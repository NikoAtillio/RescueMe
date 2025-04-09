from django.db.models import Count
from apps.shop.models import Product, CartItem, Category

def get_recommendations_for_user(user, limit=4):
    """
    Get recommendations based on product categories and popularity
    """
    # Start with an empty list to store recommended product IDs
    recommended_ids = []

    # Get main product categories
    categories = Category.objects.all()[:4]  # Limit to top categories

    # For each category, get the most popular product
    for category in categories:
        # Get most popular product in this category (based on cart additions)
        popular_in_category = Product.objects.filter(
            category=category,
            available=True
        ).annotate(
            popularity=Count('cartitem')
        ).order_by('-popularity', '-created').first()

        if popular_in_category and popular_in_category.id not in recommended_ids:
            recommended_ids.append(popular_in_category.id)

    # If we don't have enough recommendations, add featured/promoted products
    if len(recommended_ids) < limit:
        # Assuming you might add a 'featured' field to products in the future
        # For now, just get recent products
        recent_products = Product.objects.filter(
            available=True
        ).exclude(
            id__in=recommended_ids
        ).order_by('-created')

        for product in recent_products:
            if len(recommended_ids) >= limit:
                break
            recommended_ids.append(product.id)

    # Get the actual product objects in the right order
    from django.db.models import Case, When
    preserved_order = Case(*[When(id=id, then=pos) for pos, id in enumerate(recommended_ids)])

    # Return products in the preserved order, limited to requested amount
    return Product.objects.filter(id__in=recommended_ids).order_by(preserved_order)[:limit]

def get_popular_products(limit=4):
    """
    Get popular products based on cart additions
    """
    # Get products that have been added to carts most often
    popular_products = Product.objects.filter(
        available=True
    ).annotate(
        cart_count=Count('cartitem')
    ).order_by('-cart_count', '-created')[:limit]

    # If we don't have enough with cart history, add recent ones
    if popular_products.count() < limit:
        # Get IDs of products we already have
        existing_ids = list(popular_products.values_list('id', flat=True))

        # Get additional recent products
        additional_needed = limit - popular_products.count()
        recent_products = Product.objects.filter(
            available=True
        ).exclude(
            id__in=existing_ids
        ).order_by('-created')[:additional_needed]

        # Convert both querysets to lists and combine
        return list(popular_products) + list(recent_products)

    return popular_products

def get_related_products(product, limit=4):
    """
    Get products related to a specific product
    """
    # First try to get products in the same category
    related_by_category = Product.objects.filter(
        category=product.category,
        available=True
    ).exclude(id=product.id).order_by('-created')

    # If we have enough in the same category, return those
    if related_by_category.count() >= limit:
        return related_by_category[:limit]

    # Otherwise, get products for the same pet type
    related_ids = list(related_by_category.values_list('id', flat=True))

    # How many more do we need?
    additional_needed = limit - len(related_ids)

    # Get products for the same pet type
    if product.pet_type:
        related_by_pet_type = Product.objects.filter(
            pet_type=product.pet_type,
            available=True
        ).exclude(
            id=product.id
        ).exclude(
            id__in=related_ids
        ).order_by('-created')[:additional_needed]

        # Combine both sets of related products
        return list(related_by_category) + list(related_by_pet_type)

    # If we still don't have enough, just return what we have plus recent products
    additional_needed = limit - len(related_ids)
    recent_products = Product.objects.filter(
        available=True
    ).exclude(
        id=product.id
    ).exclude(
        id__in=related_ids
    ).order_by('-created')[:additional_needed]

    return list(related_by_category) + list(recent_products)