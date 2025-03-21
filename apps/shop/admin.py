from django.contrib import admin
from .models import UserPayment, Category, Product, PetType

@admin.register(UserPayment)
class UserPaymentAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'product_name',
        'price',
        'currency',
        'has_paid',
        'created_at',
        'stripe_checkout_session_id'
    ]
    list_filter = ['has_paid', 'created_at']
    list_editable = ['has_paid']
    ordering = ['-created_at']
    search_fields = ['user__username', 'product_name', 'stripe_checkout_session_id']

    readonly_fields = [
        'user',
        'stripe_customer_id',
        'stripe_checkout_session_id',
        'stripe_product_id',
        'product_name',
        'quantity',
        'price',
        'currency',
        'created_at',
        'updated_at'
    ]

    fieldsets = (
        ('User Information', {
            'fields': ('user', 'product_name', 'quantity', 'price', 'currency')
        }),
        ('Payment Status', {
            'fields': ('has_paid', 'created_at', 'updated_at')
        }),
        ('Stripe Information', {
            'fields': ('stripe_customer_id', 'stripe_checkout_session_id', 'stripe_product_id'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(PetType)
class PetTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}