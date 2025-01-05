from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class SpecialNeed(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class LivingRequirement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Animal(models.Model):
    # Basic Choice Fields
    SPECIES_CHOICES = [
        ('DOG', 'Dog'),
        ('CAT', 'Cat'),
        ('RABBIT', 'Rabbit'),
        ('HORSE', 'Horse'),
        ('BIRD', 'Bird'),
        ('SMALL_ANIMAL', 'Small Animal'),
    ]

    SIZE_CHOICES = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]

    AGE_CHOICES = [
        ('BABY', 'Baby (0-1 year)'),
        ('YOUNG', 'Young (1-3 years)'),
        ('ADULT', 'Adult (3-8 years)'),
        ('SENIOR', 'Senior (8+ years)'),
    ]

    ENERGY_LEVEL = [
        ('LOW', 'Low Energy'),
        ('MODERATE', 'Moderate Energy'),
        ('HIGH', 'High Energy'),
        ('VERY_HIGH', 'Very High Energy'),
    ]

    TRAINING_LEVEL = [
        ('NONE', 'No Training'),
        ('BASIC', 'Basic Training'),
        ('INTERMEDIATE', 'Intermediate Training'),
        ('ADVANCED', 'Advanced Training'),
    ]

    REACTIVITY_FLAGS = [
        ('DOG_FRIENDLY', 'Good with Dogs'),
        ('CAT_FRIENDLY', 'Good with Cats'),
        ('CHILD_FRIENDLY', 'Good with Children'),
        ('STRANGER_FRIENDLY', 'Good with Strangers'),
        ('LEASH_REACTIVE', 'Leash Reactive'),
        ('RESOURCE_GUARD', 'Resource Guards'),
    ]

    ADOPTION_FEE_RANGES = [
        ('FREE', 'Free'),
        ('LOW', '£1-£100'),
        ('MEDIUM', '£101-£250'),
        ('HIGH', '£251-£500'),
        ('PREMIUM', '£500+'),
    ]

    HOME_CHECK_STATUS = [
        ('REQUIRED', 'Home Check Required'),
        ('VIRTUAL', 'Virtual Home Check Accepted'),
        ('COMPLETED', 'Home Check Completed'),
        ('NOT_REQUIRED', 'No Home Check Required'),
    ]

    TRANSPORT_OPTIONS = [
        ('PROVIDED', 'Transport Available'),
        ('LOCAL_ONLY', 'Local Collection Only'),
        ('ARRANGED', 'Transport Can Be Arranged'),
        ('NOT_AVAILABLE', 'No Transport Available'),
    ]

    URGENCY_STATUS = [
        ('EMERGENCY', 'Emergency - Immediate Placement Needed'),
        ('URGENT', 'Urgent - Within 7 Days'),
        ('SOON', 'Soon - Within 30 Days'),
        ('STANDARD', 'Standard - No Immediate Rush'),
    ]

    FOSTER_STATUS = [
        ('NEEDED', 'Foster Home Needed'),
        ('TEMP', 'Temporary Foster Only'),
        ('LONG_TERM', 'Long-term Foster Needed'),
        ('NOT_NEEDED', 'Foster Not Required'),
    ]

    # Basic Info Fields
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50, choices=SPECIES_CHOICES)
    breed = models.CharField(max_length=100)
    age_category = models.CharField(max_length=50, choices=AGE_CHOICES)
    size = models.CharField(max_length=50, choices=SIZE_CHOICES)
    description = models.TextField()

    # Behavioral and Training Fields
    energy_level = models.CharField(max_length=50, choices=ENERGY_LEVEL)
    training_level = models.CharField(max_length=50, choices=TRAINING_LEVEL)
    reactivity = models.CharField(max_length=50, choices=REACTIVITY_FLAGS, blank=True)

    # Special Requirements
    special_needs = models.ManyToManyField(SpecialNeed, blank=True)
    living_requirements = models.ManyToManyField(LivingRequirement, blank=True)

    # Location and Distance
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    postcode = models.CharField(max_length=10)

    # Adoption Details
    adoption_fee = models.CharField(max_length=50, choices=ADOPTION_FEE_RANGES)
    home_check = models.CharField(max_length=50, choices=HOME_CHECK_STATUS)
    transport_available = models.CharField(max_length=50, choices=TRANSPORT_OPTIONS)
    urgency_status = models.CharField(max_length=50, choices=URGENCY_STATUS)
    foster_status = models.CharField(max_length=50, choices=FOSTER_STATUS)

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.breed} ({self.species})"

class RescueCenter(models.Model):
    RESCUE_TYPE = [
        ('ALL', 'All Animals'),
        ('DOG', 'Dogs Only'),
        ('CAT', 'Cats Only'),
        ('HORSE', 'Horses/Farm Animals'),
        ('EXOTIC', 'Exotic Animals'),
        ('WILDLIFE', 'Wildlife'),
    ]

    SERVICES_OFFERED = [
        ('ADOPTION', 'Adoption Services'),
        ('FOSTERING', 'Fostering Program'),
        ('REHABILITATION', 'Rehabilitation'),
        ('TRAINING', 'Training Services'),
        ('MEDICAL', 'Medical Services'),
        ('BOARDING', 'Boarding Services'),
        ('BEHAVIOR', 'Behavioral Support'),
        ('TRANSPORT', 'Transport Services'),
    ]

    FACILITIES = [
        ('KENNEL', 'Kennel Facilities'),
        ('CATTERY', 'Cattery'),
        ('STABLES', 'Stables'),
        ('VET', 'Veterinary Clinic'),
        ('TRAINING', 'Training Facilities'),
        ('REHAB', 'Rehabilitation Center'),
    ]

    TRANSPORT_RADIUS = [
        ('LOCAL', 'Local (up to 10 miles)'),
        ('REGIONAL', 'Regional (up to 50 miles)'),
        ('NATIONAL', 'National'),
        ('INTERNATIONAL', 'International'),
    ]

    FOSTER_NETWORK = [
        ('ACTIVE', 'Active Foster Network'),
        ('LIMITED', 'Limited Foster Network'),
        ('NEEDED', 'Foster Homes Needed'),
        ('NONE', 'No Foster Network'),
    ]

    EMERGENCY_INTAKE = [
        ('24_7', '24/7 Emergency Intake'),
        ('LIMITED', 'Limited Emergency Intake'),
        ('SCHEDULED', 'Scheduled Intake Only'),
        ('NONE', 'No Emergency Intake'),
    ]

    # Basic Info
    name = models.CharField(max_length=200)
    description = models.TextField()
    rescue_type = models.CharField(max_length=50, choices=RESCUE_TYPE)
    services = models.CharField(max_length=50, choices=SERVICES_OFFERED)
    facilities = models.CharField(max_length=50, choices=FACILITIES)

    # Contact Info
    address = models.TextField()
    postcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True)

    # Location for distance calculation
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    # Additional service fields
    transport_radius = models.CharField(max_length=50, choices=TRANSPORT_RADIUS)
    foster_network = models.CharField(max_length=50, choices=FOSTER_NETWORK)
    emergency_intake = models.CharField(max_length=50, choices=EMERGENCY_INTAKE)
    home_check_radius = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(500)],
        help_text="Maximum distance (in miles) for home checks"
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name