from django.urls import path
from . import views

app_name = 'marketplace'

urlpatterns = [
    path('animals/', views.animal_list, name='animal_list'),
    path('animals/<int:animal_id>/', views.animal_detail, name='animal_detail'),
    path('centres/', views.centre_list, name='centre_list'),
    path('centres/<int:centre_id>/', views.centre_detail, name='centre_detail'),
    path('search/', views.search_results, name='search_results'),
    path('search/autocomplete/', views.search_autocomplete, name='search_autocomplete'),
]