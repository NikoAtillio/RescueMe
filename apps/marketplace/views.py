from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Animal, RescueCentre, Contact
from apps.shop.models import Product, Wishlist
from django.contrib.auth.decorators import login_required


def animal_list(request):
    animals_list = Animal.objects.filter(is_available=True)
    
    # Filter by species if provided
    species = request.GET.get('species')
    if species:
        animals_list = animals_list.filter(species=species)
    
    # Filter by size if provided
    size = request.GET.get('size')
    if size:
        animals_list = animals_list.filter(size=size)
    
    # Filter by age if provided
    age = request.GET.get('age')
    if age:
        animals_list = animals_list.filter(age_category=age)
    
    # Filter by rescue centre if provided
    rescue_centre = request.GET.get('rescue_centre')
    if rescue_centre:
        animals_list = animals_list.filter(rescue_centre_id=rescue_centre)
    
    # Pagination
    paginator = Paginator(animals_list, 12)  # Show 12 animals per page
    page = request.GET.get('page')
    try:
        animals = paginator.page(page)
    except PageNotAnInteger:
        animals = paginator.page(1)
    except EmptyPage:
        animals = paginator.page(paginator.num_pages)
    
    context = {
        'animals': animals,
        'species_choices': Animal.SPECIES_CHOICES,
        'size_choices': Animal.SIZE_CHOICES,
        'age_choices': Animal.AGE_CHOICES,
    }
    
    return render(request, 'marketplace/animal_list.html', context)

def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)

    # Get related animals (same species)
    related_animals = Animal.objects.filter(
        species=animal.species,
        is_available=True
    ).exclude(pk=animal.pk)[:4]

    # Get user favourites if user is authenticated
    user_favourites = []
    if request.user.is_authenticated:
        from accounts.models import Favourite
        user_favourites = [fav.animal for fav in Favourite.objects.filter(user=request.user)]

    context = {
        'animal': animal,
        'related_animals': related_animals,
        'user_favourites': user_favourites,
    }

    return render(request, 'marketplace/animal_detail.html', context)

def centre_list(request):
    centres_list = RescueCentre.objects.all()
    
    # Filter by rescue type if provided
    rescue_type = request.GET.get('rescue_type')
    if rescue_type:
        centres_list = centres_list.filter(rescue_type=rescue_type)
    
    # Filter by services if provided
    services = request.GET.get('services')
    if services:
        centres_list = centres_list.filter(services=services)
    
    # Search by name or location
    search = request.GET.get('search')
    if search:
        centres_list = centres_list.filter(
            name__icontains=search
        ) | centres_list.filter(
            address__icontains=search
        ) | centres_list.filter(
            postcode__icontains=search
        )
    
    # Sort if provided
    sort = request.GET.get('sort')
    if sort:
        centres_list = centres_list.order_by(sort)
    
    # Count centres by type for sidebar
    all_count = RescueCentre.objects.filter(rescue_type='ALL').count()
    dog_count = RescueCentre.objects.filter(rescue_type='DOG').count()
    cat_count = RescueCentre.objects.filter(rescue_type='CAT').count()
    horse_count = RescueCentre.objects.filter(rescue_type='HORSE').count()
    exotic_count = RescueCentre.objects.filter(rescue_type='EXOTIC').count()
    wildlife_count = RescueCentre.objects.filter(rescue_type='WILDLIFE').count()
    
    # Pagination
    paginator = Paginator(centres_list, 10)  # Show 10 centres per page
    page = request.GET.get('page')
    try:
        centres = paginator.page(page)
    except PageNotAnInteger:
        centres = paginator.page(1)
    except EmptyPage:
        centres = paginator.page(paginator.num_pages)
    
    context = {
        'centres': centres,
        'all_count': all_count,
        'dog_count': dog_count,
        'cat_count': cat_count,
        'horse_count': horse_count,
        'exotic_count': exotic_count,
        'wildlife_count': wildlife_count,
    }
    
    return render(request, 'marketplace/centre_list.html', context)

def centre_detail(request, pk):
    centre = get_object_or_404(RescueCentre, pk=pk)
    
    # Get animals from this centre
    animals_list = Animal.objects.filter(rescue_centre=centre, is_available=True)
    
    # Pagination for animals
    paginator = Paginator(animals_list, 9)  # Show 9 animals per page
    page = request.GET.get('page')
    try:
        animals = paginator.page(page)
    except PageNotAnInteger:
        animals = paginator.page(1)
    except EmptyPage:
        animals = paginator.page(paginator.num_pages)
    
    context = {
        'centre': centre,
        'animals': animals,
    }
    
    return render(request, 'marketplace/centre_detail.html', context)

def search_results(request):
    """Handle search requests"""
    query = request.GET.get('q', '')
    species = request.GET.get('species', '')
    size = request.GET.get('size', '')
    age = request.GET.get('age', '')

    animals = Animal.objects.filter(is_available=True)
    if query:
        from django.db.models import Q
        animals = animals.filter(Q(name__icontains=query) | Q(breed__icontains=query))
    if species:
        animals = animals.filter(species=species)
    if size:
        animals = animals.filter(size=size)
    if age:
        animals = animals.filter(age_category=age)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_to_string('marketplace/search_results.html', {
            'animals': animals
        })
        return JsonResponse({'html': html}, safe=False)

    context = {
        'animals': animals,
        'query': query,
        'species': species,
        'size': size,
        'age': age,
        'species_choices': Animal.SPECIES_CHOICES,
        'size_choices': Animal.SIZE_CHOICES,
        'age_choices': Animal.AGE_CHOICES,
    }
    
    return render(request, 'marketplace/search_results.html', context)
