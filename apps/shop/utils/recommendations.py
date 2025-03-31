from django.db.models import Count
from apps.shop.models import Product, UserPayment
from apps.accounts.models import Favourite

def get_recommendations_for_user(user, limit=4):
    """
    Generate personalised product recommendations for a user based on:
    1. Their purchase history
    2. Their favourite animals
    3. Popular products in categories they've shown interest in
    """
    if not user.is_authenticated:
        return get_popular_products(limit)

    # Start with an empty queryset
    recommended_products = Product.objects.none()

    # 1. Get products similar to what they've purchased
    purchased_products = UserPayment.objects.filter(
        user=user,
        has_paid=True
    ).values_list('stripe_product_id', flat=True)

    if purchased_products:
        # Find products in the same categories as purchased products
        purchased_categories = Product.objects.filter(
            id__in=purchased_products
        ).values_list('category', flat=True)

        category_recommendations = Product.objects.filter(
            category__in=purchased_categories,
            available=True
        ).exclude(id__in=purchased_products)

        recommended_products = recommended_products.union(category_recommendations)

    # 2. Get products based on their favourite animals
    try:
        favourite_animals = user.favourites.all()
        if favourite_animals:
            # Get the species of their favourite animals
            pet_types = set()
            for favourite in favourite_animals:
                if favourite.animal.species == 'DOG':
                    pet_types.add('dog')
                elif favourite.animal.species == 'CAT':
                    pet_types.add('cat')
                # Add more mappings as needed

            # Find products for those pet types
            pet_type_recommendations = Product.objects.filter(
                pet_type__slug__in=pet_types,
                available=True
            )

            recommended_products = recommended_products.union(pet_type_recommendations)
    except:
        # User might not have favourites attribute
        pass

    # If we still don't have enough recommendations, add popular products
    if recommended_products.count() < limit:
        popular_products = get_popular_products(limit)
        recommended_products = recommended_products.union(popular_products)

    # Return a limited, distinct set of recommendations
    return recommended_products.distinct()[:limit]

def get_popular_products(limit=4):
    """Get popular products based on purchase history"""
    # Get products that have been purchased most often
    popular_products = Product.objects.filter(
        available=True
    ).annotate(
        purchase_count=Count('userpayment')
    ).order_by('-purchase_count')[:limit]

    # If there aren't enough products with purchase history, add some recent ones
    if popular_products.count() < limit:
        recent_products = Product.objects.filter(
            available=True
        ).order_by('-created')[:limit - popular_products.count()]

        # Combine the querysets
        popular_products = list(popular_products) + list(recent_products)

    return popular_products[:limit]

def get_related_products(product, limit=4):
    """Get products related to a specific product"""
    # Get products in the same category
    category_products = Product.objects.filter(
        category=product.category,
        available=True
    ).exclude(id=product.id)[:limit]

    # If we don't have enough, add products for the same pet type
    if category_products.count() < limit:
        pet_type_products = Product.objects.filter(
            pet_type=product.pet_type,
            available=True
        ).exclude(
            id=product.id
        ).exclude(
            id__in=[p.id for p in category_products]
        )[:limit - category_products.count()]

        # Combine the querysets
        related_products = list(category_products) + list(pet_type_products)
    else:
        related_products = list(category_products)

    return related_products[:limit]