from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings

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

def who_are_we(request):
    try:
        context = {
            'title': 'Who Are We | Rescue Me',
            'static_url': settings.STATIC_URL,
        }
        return render(request, 'who-are-we.html', context)
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

def get_in_touch(request):
    try:
        context = {
            'title': 'Contact Us | Rescue Me',
            'static_url': settings.STATIC_URL,
        }
        return render(request, 'get-in-touch.html', context)
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