from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Product, PetType, Cart, CartItem, UserPayment, Wishlist, SavedSearch
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

    return render(request, 'core/shop.html', {
        'categories': categories,
        'pet_types': pet_types,
        'featured_products': featured_products
    })


def products(request, pet_type=None):
    """View for listing products with advanced filtering"""
    category = None
    pet_type_obj = None
    categories = Category.objects.all()
    pet_types = PetType.objects.all()
    products = Product.objects.filter(available=True)

    # Basic filters
    if pet_type:
        pet_type_obj = get_object_or_404(PetType, slug=pet_type)
        products = products.filter(pet_type=pet_type_obj)

    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # Advanced filters
    # Price range filter
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        try:
            products = products.filter(price__gte=float(min_price))
        except ValueError:
            pass
    if max_price:
        try:
            products = products.filter(price__lte=float(max_price))
        except ValueError:
            pass

    # Search by name or description
    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    # Sort options
    sort = request.GET.get('sort', '')
    if sort == 'price_low':
        products = products.order_by('price')
    elif sort == 'price_high':
        products = products.order_by('-price')
    elif sort == 'newest':
        products = products.order_by('-created')
    elif sort == 'name':
        products = products.order_by('name')

    # Get unique values for filters
    all_prices = Product.objects.filter(available=True).values_list('price', flat=True).distinct().order_by('price')
    min_db_price = all_prices.first() if all_prices else 0
    max_db_price = all_prices.last() if all_prices else 100

    # Get personalised recommendations
    recommended_products = get_recommendations_for_user(request.user)

    return render(request, 'shop/products/products.html', {
        'category': category,
        'pet_type': pet_type_obj,
        'categories': categories,
        'pet_types': pet_types,
        'products': products,
        'recommended_products': recommended_products,
        'search_query': search_query,
        'min_db_price': min_db_price,
        'max_db_price': max_db_price,
        'min_price': min_price,
        'max_price': max_price,
        'sort': sort,
    })

def product_detail(request, slug):
    """View for showing product details"""
    product = get_object_or_404(Product, slug=slug, available=True)
    cart_item_form = CartItemForm()

    # Get related products
    related_products = get_related_products(product)

    # Get personalised recommendations
    recommended_products = get_recommendations_for_user(request.user)

    # Get user's wishlist products
    user_wishlist_products = []
    if request.user.is_authenticated:
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        user_wishlist_products = wishlist.products.all()

    return render(request, 'shop/products/product_detail.html', {
        'product': product,
        'cart_item_form': cart_item_form,
        'related_products': related_products,
        'recommended_products': recommended_products,
        'user_wishlist_products': user_wishlist_products
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

    return render(request, 'shop/products/product_list.html', context)


def product_quick_view(request, product_id):
    """Quick view modal for a product"""
    product = get_object_or_404(Product, id=product_id, available=True)

    # Get user's wishlist products
    user_wishlist_products = []
    if request.user.is_authenticated:
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        user_wishlist_products = wishlist.products.all()

    return render(request, 'shop/products/quick_view.html', {
        'product': product,
        'user_wishlist_products': user_wishlist_products
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
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    # Calculate total price for each item
    for item in cart_items:
        item.total_price = item.product.price * item.quantity

    return render(request, 'shop/payment/cart.html', {
        'cart': cart,
        'cart_items': cart_items,
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


# Wishlist

@login_required
def wishlist(request):
    """Display user's wishlist"""
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    products = wishlist.products.all()
    return render(request, 'shop/products/wishlist.html', {
        'wishlist': wishlist,
        'products': products
    })

@login_required
def add_to_wishlist(request, product_id):
    """Add a product to user's wishlist"""
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    messages.success(request, f"{product.name} has been added to your wishlist.")
    return redirect(request.META.get('HTTP_REFERER', 'shop:products'))

@login_required
def remove_from_wishlist(request, product_id):
    """Remove a product from user's wishlist"""
    product = get_object_or_404(Product, id=product_id)
    wishlist = get_object_or_404(Wishlist, user=request.user)
    wishlist.products.remove(product)
    messages.success(request, f"{product.name} has been removed from your wishlist.")
    return redirect(request.META.get('HTTP_REFERER', 'shop:wishlist'))


# Search Products

def search_autocomplete(request):
    """API endpoint for search autocomplete suggestions"""
    query = request.GET.get('q', '')
    suggestions = []

    if query and len(query) >= 2:
        # Get product name suggestions
        product_suggestions = Product.objects.filter(
            name__icontains=query,
            available=True
        ).values_list('name', flat=True)[:5]

        # Get category suggestions
        category_suggestions = Category.objects.filter(
            name__icontains=query
        ).values_list('name', flat=True)[:3]

        # Get pet type suggestions
        pet_type_suggestions = PetType.objects.filter(
            name__icontains=query
        ).values_list('name', flat=True)[:3]

        # Combine suggestions
        suggestions = list(product_suggestions)

        for cat in category_suggestions:
            suggestions.append(f"Category: {cat}")

        for pet in pet_type_suggestions:
            suggestions.append(f"Pet Type: {pet}")

    return JsonResponse({'suggestions': suggestions})


@login_required
def save_search(request):
    """Save the current search query"""
    if request.method == 'POST':
        name = request.POST.get('search_name')
        query_string = request.POST.get('query_string')

        if name and query_string:
            SavedSearch.objects.create(
                user=request.user,
                name=name,
                query_string=query_string
            )
            messages.success(request, f'Search "{name}" has been saved.')

    return redirect(request.META.get('HTTP_REFERER', 'shop:products'))

@login_required
def saved_searches(request):
    """View for managing saved searches"""
    searches = SavedSearch.objects.filter(user=request.user)
    return render(request, 'shop/products/saved_searches.html', {'searches': searches})

@login_required
def delete_saved_search(request, search_id):
    """Delete a saved search"""
    search = get_object_or_404(SavedSearch, id=search_id, user=request.user)
    search.delete()
    messages.success(request, f'Search "{search.name}" has been deleted.')
    return redirect('shop:saved_searches')