from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('our-mission/', views.our_mission, name='our_mission'),
    path('about-us/', views.about_us, name='about_us'),
    path('shop/', views.shop, name='shop'),
    path('get-in-touch/', views.get_in_touch, name='get_in_touch'),
    path('faq/', views.faq, name='faq'),
    path('partners/', views.partners, name='partners'),
    path('test/', views.test_view, name='test'),
]