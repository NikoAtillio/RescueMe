from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us/', views.about_us, name='about-us'),
    path('our-mission/', views.our_mission, name='our-mission'),
    path('shop/', views.shop, name='shop'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
]