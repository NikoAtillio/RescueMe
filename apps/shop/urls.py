from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.shop_home, name='shop_home'),
    path('products/', views.products, name='products'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('products/pet-type/<str:pet_type>/', views.products, name='product_list_by_pet_type'),

    # Cart URLs
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),

    # Payment URLs
    path('checkout/', views.checkout, name='checkout'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('payment/cancel/', views.payment_cancel, name='payment_cancel'),
    path('payment/error/', views.payment_error, name='payment_error'),
]