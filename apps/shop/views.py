from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Product, PetType, Cart, CartItem, UserPayment
from .forms import CartItemForm, CheckoutForm
import stripe
from django.conf import settings
from django.http import JsonResponse
from .utils.recommendations import get_recommendations_for_user, get_related_products
from django.db.models import Q


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


def products(request, pet_type=None):
    """View for listing products, optionally filtered by pet type or category"""
    category = None
    pet_type_obj = None
    categories = Category.objects.all()
    pet_types = PetType.objects.all()
    products = Product.objects.filter(available=True)

    # Filter by pet type if provided
    if pet_type:
        pet_type_obj = get_object_or_404(PetType, slug=pet_type)
        products = products.filter(pet_type=pet_type_obj)

    # Filter by category if provided in query params
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # Get personalised recommendations
    recommended_products = get_recommendations_for_user(request.user)

    return render(request, 'shop/products.html', {
        'category': category,
        'pet_type': pet_type_obj,
        'categories': categories,
        'pet_types': pet_types,
        'products': products,
        'recommended_products': recommended_products
    })

def product_detail(request, slug):
    """View for showing product details"""
    product = get_object_or_404(Product, slug=slug, available=True)
    cart_item_form = CartItemForm()

    # Get related products
    related_products = get_related_products(product)

    # Get personalised recommendations
    recommended_products = get_recommendations_for_user(request.user)

    return render(request, 'shop/product_detail.html', {
        'product': product,
        'cart_item_form': cart_item_form,
        'related_products': related_products,
        'recommended_products': recommended_products
    })

def product_list(request):
    products = Product.objects.filter(available=True)

    # Handle search
    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    # Handle sorting
    sort = request.GET.get('sort', '')
    if sort == 'name':
        products = products.order_by('name')
    elif sort == 'price-low':
        products = products.order_by('price')
    elif sort == 'price-high':
        products = products.order_by('-price')
    elif sort == 'newest':
        products = products.order_by('-created')

    context = {
        'products': products,
        'search_query': search_query,
    }

    return render(request, 'shop/product_list.html', context)


def product_quick_view(request, product_id):
    product = get_object_or_404(Product, id=product_id, available=True)
    return render(request, 'shop/quick_view.html', {'product': product})

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
        return redirect('shop:products')

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