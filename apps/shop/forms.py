from django import forms
from .models import Product, CartItem

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'pet_type', 'description', 'price', 'stock', 'available', 'image']

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']

class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    address = forms.CharField(max_length=250)
    postal_code = forms.CharField(max_length=20)
    city = forms.CharField(max_length=100)