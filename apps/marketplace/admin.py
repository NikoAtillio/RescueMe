from django.contrib import admin
from django.utils.html import format_html
from .models import Animal, RescueCentre, Contact, SpecialNeed, LivingRequirement, AnimalImage, CentreImage

# Custom admin site header and title
admin.site.site_header = 'Rescue Me Administration'
admin.site.site_title = 'Rescue Me Portal'
admin.site.index_title = 'Welcome to Rescue Me Portal'

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'breed', 'age_category', 'size', 'status_tag')
    list_filter = ('species', 'age_category', 'size', 'is_available')
    search_fields = ('name', 'breed', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'species', 'breed', 'age_category', 'size', 'description')
        }),
        ('Characteristics', {
            'fields': ('energy_level', 'training_level', 'reactivity')
        }),
        ('Special Considerations', {
            'fields': ('special_needs', 'living_requirements')
        }),
        ('Location', {
            'fields': ('postcode', 'latitude', 'longitude')
        }),
        ('Adoption Details', {
            'fields': ('adoption_fee', 'home_check', 'transport_available', 
                      'urgency_status', 'foster_status', 'is_available')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def status_tag(self, obj):
        if obj.is_available:
            color = 'green'
            status = 'Available'
        else:
            color = 'red'
            status = 'Not Available'
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            color,
            status
        )
    status_tag.short_description = 'Status'

@admin.register(RescueCentre)
class RescueCentreAdmin(admin.ModelAdmin):
    list_display = ('name', 'rescue_type', 'postcode', 'emergency_intake_status')
    list_filter = ('rescue_type', 'services', 'facilities', 'emergency_intake')
    search_fields = ('name', 'description', 'postcode')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'rescue_type')
        }),
        ('Services & Facilities', {
            'fields': ('services', 'facilities')
        }),
        ('Contact Information', {
            'fields': ('address', 'postcode', 'phone', 'email', 'website')
        }),
        ('Location', {
            'fields': ('latitude', 'longitude')
        }),
        ('Service Coverage', {
            'fields': ('transport_radius', 'foster_network', 
                      'emergency_intake', 'home_check_radius')
        }),
    )

    def emergency_intake_status(self, obj):
        colors = {
            '24_7': 'green',
            'LIMITED': 'orange',
            'SCHEDULED': 'blue',
            'NONE': 'red'
        }
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            colors.get(obj.emergency_intake, 'black'),
            obj.get_emergency_intake_display()
        )
    emergency_intake_status.short_description = 'Emergency Intake'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'rescue_centre', 'phone_number', 'email')
    list_filter = ('rescue_centre',)
    search_fields = ('name', 'phone_number', 'email')

@admin.register(SpecialNeed)
class SpecialNeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(LivingRequirement)
class LivingRequirementAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    
@admin.register(AnimalImage)
class AnimalImageAdmin(admin.ModelAdmin):
    list_display = ('animal', 'is_primary', 'uploaded_at')
    list_filter = ('is_primary', 'uploaded_at')
    search_fields = ('animal__name', 'caption')

@admin.register(CentreImage)
class CentreImageAdmin(admin.ModelAdmin):
    list_display = ('rescue_centre', 'is_primary', 'uploaded_at')
    list_filter = ('is_primary', 'uploaded_at')
    search_fields = ('rescue_centre__name', 'caption')