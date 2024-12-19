"""
URL configuration for my_project project.
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from hello_world import views as index_views

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

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)