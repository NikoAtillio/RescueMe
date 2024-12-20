from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings

@csrf_exempt
def test_view(request):
    try:
        context = {
            'title': 'Static Test | Rescue Me',
            'STATIC_URL': settings.STATIC_URL,
            'BASE_DIR': settings.BASE_DIR,
            'static_url': settings.STATIC_URL,
        }
        return render(request, 'test.html', context)
    except Exception as e:
        return handle_error(request, e)

# Create your views here.
def index(request):
    try:
        context = {
            'title': 'Home | Rescue Me',
            'static_url': settings.STATIC_URL,
        }
        return render(request, 'index.html', context)
    except Exception as e:
        return handle_error(request, e)

def search(request):
    try:
        context = {
            'title': 'Search | Rescue Me',
            'static_url': settings.STATIC_URL,
        }
        return render(request, 'search.html', context)
    except Exception as e:
        return handle_error(request, e)

def our_mission(request):
    try:
        context = {
            'title': 'Our Mission | Rescue Me',
            'static_url': settings.STATIC_URL,
        }
        return render(request, 'our-mission.html', context)
    except Exception as e:
        return handle_error(request, e)

def about_us(request):
    try:
        context = {
            'title': 'About Us | Rescue Me',
            'static_url': settings.STATIC_URL,
        }
        return render(request, 'about-us.html', context)
    except Exception as e:
        return handle_error(request, e)

def shop(request):
    try:
        context = {
            'title': 'Shop | Rescue Me',
            'static_url': settings.STATIC_URL,
        }
        return render(request, 'shop.html', context)
    except Exception as e:
        return handle_error(request, e)

def gecontact(request):
    try:
        context = {
            'title': 'Contact Us | Rescue Me',
            'static_url': settings.STATIC_URL,
        }
        return render(request, 'contact.html', context)
    except Exception as e:
        return handle_error(request, e)

def faq(request):
    try:
        context = {
            'title': 'FAQ | Rescue Me',
            'static_url': settings.STATIC_URL,
        }
        return render(request, 'faq.html', context)
    except Exception as e:
        return handle_error(request, e)

def partners(request):
    try:
        context = {
            'title': 'Partners | Rescue Me',
            'static_url': settings.STATIC_URL,
        }
        return render(request, 'partners.html', context)
    except Exception as e:
        return handle_error(request, e)

# Error handlers
def handle_error(request, error):
    if settings.DEBUG:
        return HttpResponse(f"Error: {str(error)}")
    return render(request, '500.html', status=500)

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)