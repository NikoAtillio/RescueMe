from django.contrib import admin
from .models import Animal, RescueCenter, SpecialNeed, LivingRequirement

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'breed', 'age_category', 'size', 'is_available')
    list_filter = ('species', 'size', 'age_category', 'is_available')
    search_fields = ('name', 'breed', 'description')
    list_per_page = 20

@admin.register(RescueCenter)
class RescueCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'rescue_type', 'postcode', 'phone')
    list_filter = ('rescue_type', 'services', 'facilities')
    search_fields = ('name', 'description', 'postcode')
    list_per_page = 20

@admin.register(SpecialNeed)
class SpecialNeedAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')

@admin.register(LivingRequirement)
class LivingRequirementAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')