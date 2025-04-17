from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/', views.about_us, name='about_us'),
    path('our_mission/', views.our_mission, name='our_mission'),
    path('partners/', views.partners, name='partners'),
    path('charities/', views.charities, name='charities'),
    path('about_you/', views.about_you, name='about_you'),
    path('checklists/', views.checklists, name='checklists'),
    path('processes/', views.processes, name='processes'),
    path('find_your_match/', views.find_your_match, name='find_your_match'),
    path('shop/', views.shop, name='shop'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('newsletter-signup/', views.newsletter_signup, name='newsletter_signup'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('donate/', views.donate, name='donate'),
]