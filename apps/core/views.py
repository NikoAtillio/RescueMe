from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q

from apps.shop.models import Product
from apps.marketplace.models import Animal, RescueCentre  # Fixed the capitalization
from .models import Contact

def index(request):
    """View for the home page"""
    # Get featured products, animals, and rescue centers for the homepage
    featured_products = Product.objects.filter(featured=True)[:4] if 'featured' in [f.name for f in Product._meta.get_fields()] else Product.objects.all()[:4]

    # Your Animal model doesn't have a 'status' field, so let's update this query
    recent_animals = Animal.objects.filter(is_available=True).order_by('-created_at')[:4]

    # Fixed the model name
    rescue_centers = RescueCentre.objects.all()[:3]

    context = {
        'featured_products': featured_products,
        'recent_animals': recent_animals,
        'rescue_centers': rescue_centers,
    }
    return render(request, 'core/index.html', context)

def about_us(request):
    """View for the about us page"""
    return render(request, 'core/about-us.html')

def our_mission(request):
    """View for the our mission page"""
    return render(request, 'core/our-mission.html')

def partners(request):
    """View for the partners page"""
    return render(request, 'core/partners.html')

def faq(request):
    """View for the FAQ page"""
    return render(request, 'core/faq.html')

def shop(request):
    """View for the shop page"""
    return render(request, 'core/shop.html')

def contact(request):
    """View for the contact page and form handling"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to database
        contact = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Send email notification
        try:
            send_mail(
                f'New Contact Form Submission: {subject}',
                f'From: {name} ({email})\n\n{message}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent. We will get back to you soon!')
        except Exception as e:
            messages.error(request, 'There was an error sending your message. Please try again later.')

        return redirect('core:contact')

    return render(request, 'core/contact.html')

def search(request):
    """View for the search page"""
    query = request.GET.get('q', '')

    if query:
        # Search products
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

        # Search animals
        animals = Animal.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(breed__icontains=query)
        )

        # Search rescue centers - fixed the model name and removed 'location' field
        # which doesn't exist in your model
        centers = RescueCentre.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(address__icontains=query)  # Changed from 'location' to 'address'
        )
    else:
        products = Product.objects.none()
        animals = Animal.objects.none()
        centers = RescueCentre.objects.none()  # Fixed the model name

    context = {
        'query': query,
        'products': products,
        'animals': animals,
        'centers': centers,
    }

    return render(request, 'core/search.html', context)

def handler404(request, exception):
    """Custom 404 error handler"""
    return render(request, 'core/404.html', status=404)

def handler500(request):
    """Custom 500 error handler"""
    return render(request, 'core/500.html', status=500)