from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Product, PetType, Cart, CartItem, UserPayment
from .forms import CartItemForm, CheckoutForm
import stripe
from django.conf import settings
from django.http import JsonResponse

def shop_home(request):
    """Main shop page view"""
    categories = Category.objects.all()
    pet_types = PetType.objects.all()
    featured_products = Product.objects.filter(available=True)[:6]  # Get some featured products

    return render(request, 'shop/shop.html', {
        'categories': categories,
        'pet_types': pet_types,
        'featured_products': featured_products
    })

def product_list(request, category_slug=None, pet_type_slug=None):
    """View for listing products, optionally filtered by category or pet type"""
    category = None
    pet_type = None
    categories = Category.objects.all()
    pet_types = PetType.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    if pet_type_slug:
        pet_type = get_object_or_404(PetType, slug=pet_type_slug)
        products = products.filter(pet_type=pet_type)

    return render(request, 'shop/products/products.html', {
        'category': category,
        'pet_type': pet_type,
        'categories': categories,
        'pet_types': pet_types,
        'products': products
    })

def product_detail(request, slug):
    """View for showing product details"""
    product = get_object_or_404(Product, slug=slug, available=True)
    cart_item_form = CartItemForm()

    return render(request, 'shop/products/product_detail.html', {
        'product': product,
        'cart_item_form': cart_item_form
    })

@login_required
def cart_add(request, product_id):
    """Add a product to the cart"""
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('shop:cart_detail')

@login_required
def cart_remove(request, product_id):
    """Remove a product from the cart"""
    cart = Cart.objects.get(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    cart_item.delete()

    return redirect('shop:cart_detail')

@login_required
def cart_detail(request):
    """View cart contents"""
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'shop/payment/cart.html', {
        'cart_items': cart_items,
        'total': total
    })

@login_required
def checkout(request):
    """Checkout process"""
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    if not cart_items:
        return redirect('shop:product_list')

    total = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Process the order
            # Redirect to payment
            return redirect('shop:payment_success')
    else:
        form = CheckoutForm()

    return render(request, 'shop/payment/checkout.html', {
        'form': form,
        'cart_items': cart_items,
        'total': total
    })

@login_required
def payment_success(request):
    """Handle successful payment"""
    # Process successful payment
    return render(request, 'shop/payment/success.html')

@login_required
def payment_cancel(request):
    """Handle cancelled payment"""
    # Handle cancelled payment
    return render(request, 'shop/payment/cancel.html')

@login_required
def payment_error(request):
    """Handle payment errors"""
    # Handle payment errors
    return render(request, 'shop/payment/error.html')