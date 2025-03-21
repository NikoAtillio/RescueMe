# shop/context_processors.py
from .models import Cart, CartItem

def cart_items_count(request):
    """
    Adds the number of items in the user's cart to the template context.
    """
    if request.user.is_authenticated:
        # Get the user's cart
        cart, created = Cart.objects.get_or_create(user=request.user)
        # Count the number of items in the cart
        cart_items_count = CartItem.objects.filter(cart=cart).count()
    else:
        # For anonymous users, you can use session-based cart logic
        cart_items_count = 0  # Replace with your session-based logic if needed

    return {
        'cart_items_count': cart_items_count,
    }