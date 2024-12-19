"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hello_world import views as index_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin URL
    path('admin/', admin.site.urls),
    
    # Main pages
    path('', index_views.index, name='index'),
    path('who-are-we/', index_views.who_are_we, name='who_are_we'),
    path('our-mission/', index_views.our_mission, name='our_mission'),
    path('about-us/', index_views.about_us, name='about_us'),
    path('shop/', index_views.shop, name='shop'),
    path('get-in-touch/', index_views.get_in_touch, name='get_in_touch'),
    path('faq/', index_views.faq, name='faq'),
    path('partners/', index_views.partners, name='partners'),
] 

# Add this to serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)