from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # Produts URLs
    
    path('', views.shop_home, name='shop_home'),
    path('products/', views.products, name='products'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('products/pet-type/<str:pet_type>/', views.products, name='product_list_by_pet_type'),
    path('product/<int:product_id>/quick-view/', views.product_quick_view, name='product_quick_view'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),

    # Cart URLs
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),

    # Payment URLs
    path('checkout/', views.checkout, name='checkout'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('payment/cancel/', views.payment_cancel, name='payment_cancel'),
    path('payment/error/', views.payment_error, name='payment_error'),
    
    # Search
    path('search/autocomplete/', views.search_autocomplete, name='search_autocomplete'),
    path('searches/save/', views.save_search, name='save_search'),
    path('searches/', views.saved_searches, name='saved_searches'),
    path('searches/delete/<int:search_id>/', views.delete_saved_search, name='delete_saved_search'),
]