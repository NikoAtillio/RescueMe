from django.urls import path
from . import views

app_name = 'hello_world'

urlpatterns = [
    path('test/', views.test_view, name='test'),
    path('', views.index, name='index'),
    path('who-are-we/', views.who_are_we, name='who_are_we'),
    path('our-mission/', views.our_mission, name='our_mission'),
    path('about-us/', views.about_us, name='about_us'),
    path('shop/', views.shop, name='shop'),
    path('get-in-touch/', views.get_in_touch, name='get_in_touch'),
    path('faq/', views.faq, name='faq'),
    path('partners/', views.partners, name='partners'),
]