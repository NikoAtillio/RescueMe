from django.urls import path
from . import views

app_name = 'marketplace'

urlpatterns = [
    path('animals/', views.animal_list, name='animal_list'),
    path('animals/<int:animal_id>/', views.animal_detail, name='animal_detail'),
    path('centres/', views.centre_list, name='centre_list'),
    path('centres/<int:centre_id>/', views.centre_detail, name='centre_detail'),
    path('search/', views.search_results, name='search_results'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]