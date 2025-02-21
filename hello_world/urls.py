from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'), 
    path('blog/', views.blog, name='blog'),  
    path('our-mission/', views.our_mission, name='our_mission'),
    path('about-us/', views.about_us, name='about_us'),
    path('shop/', views.shop, name='shop'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('partners/', views.partners, name='partners'),
    path('test/', views.test_view, name='test'),
]