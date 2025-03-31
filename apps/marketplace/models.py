from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class SpecialNeed(models.Model):
    name = models.CharField(max_length=100, default="Unnamed Need")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class LivingRequirement(models.Model):
    name = models.CharField(max_length=100, default="Unnamed Requirement")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class RescueCentre(models.Model):
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
        ('REHAB', 'Rehabilitation Centre'),
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
    name = models.CharField(max_length=200, default="Unnamed Centre")
    description = models.TextField(default="No description provided")
    rescue_type = models.CharField(max_length=50, choices=RESCUE_TYPE, default='ALL')
    services = models.CharField(max_length=50, choices=SERVICES_OFFERED, default='ADOPTION')
    facilities = models.CharField(max_length=50, choices=FACILITIES, default='KENNEL')

    # Contact Info
    address = models.TextField(default="Address pending")
    postcode = models.CharField(max_length=10, default="Unknown")
    phone = models.CharField(max_length=20, default="TBD")
    email = models.EmailField(default="pending@example.com")
    website = models.URLField(blank=True)

    # Location for distance calculation
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)

    # Additional service fields
    transport_radius = models.CharField(max_length=50, choices=TRANSPORT_RADIUS, default='LOCAL')
    foster_network = models.CharField(max_length=50, choices=FOSTER_NETWORK, default='NONE')
    emergency_intake = models.CharField(max_length=50, choices=EMERGENCY_INTAKE, default='SCHEDULED')
    home_check_radius = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(500)],
        help_text="Maximum distance (in miles) for home checks",
        default=20
    )

    class Meta:
        ordering = ['name']

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
    name = models.CharField(max_length=100, default="Unnamed")
    species = models.CharField(max_length=50, choices=SPECIES_CHOICES, default='DOG')
    breed = models.CharField(max_length=100, default="Unknown")
    age_category = models.CharField(max_length=50, choices=AGE_CHOICES, default='ADULT')
    size = models.CharField(max_length=50, choices=SIZE_CHOICES, default='M')
    description = models.TextField(default="No description provided")

    # Behavioral and Training Fields
    energy_level = models.CharField(max_length=50, choices=ENERGY_LEVEL, default='MODERATE')
    training_level = models.CharField(max_length=50, choices=TRAINING_LEVEL, default='BASIC')
    reactivity = models.CharField(max_length=50, choices=REACTIVITY_FLAGS, blank=True, default='DOG_FRIENDLY')

    # Special Requirements
    special_needs = models.ManyToManyField(SpecialNeed, blank=True)
    living_requirements = models.ManyToManyField(LivingRequirement, blank=True)

    # Location and Distance
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    postcode = models.CharField(max_length=10, default="Unknown")

    # Rescue Centre Relationship
    rescue_centre = models.ForeignKey(RescueCentre, on_delete=models.CASCADE, related_name='animals', null=True)

    # Adoption Details
    adoption_fee = models.CharField(max_length=50, choices=ADOPTION_FEE_RANGES, default='LOW')
    home_check = models.CharField(max_length=50, choices=HOME_CHECK_STATUS, default='REQUIRED')
    transport_available = models.CharField(max_length=50, choices=TRANSPORT_OPTIONS, default='LOCAL_ONLY')
    urgency_status = models.CharField(max_length=50, choices=URGENCY_STATUS, default='STANDARD')
    foster_status = models.CharField(max_length=50, choices=FOSTER_STATUS, default='NOT_NEEDED')

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.breed} ({self.species})"


class Contact(models.Model):
    name = models.CharField(max_length=100, default="Unnamed Contact")
    phone_number = models.CharField(max_length=50, default="No phone provided")
    email = models.CharField(max_length=100, default="no.email@example.com")
    rescue_centre = models.ForeignKey(RescueCentre, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AnimalImage(models.Model):
    """Model for storing multiple images for an animal"""
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='animal_images/')
    is_primary = models.BooleanField(default=False)
    caption = models.CharField(max_length=200, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_primary', '-uploaded_at']

    def __str__(self):
        return f"Image for {self.animal.name}"


class CentreImage(models.Model):
    """Model for storing multiple images for a rescue centre"""
    rescue_centre = models.ForeignKey(RescueCentre, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='centre_images/')
    is_primary = models.BooleanField(default=False)
    caption = models.CharField(max_length=200, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_primary', '-uploaded_at']

    def __str__(self):
        return f"Image for {self.rescue_centre.name}"

def animal_list(request):
    animals_list = Animal.objects.filter(is_available=True)

    # Filter by species if provided
    species = request.GET.get('species')
    if species:
        animals_list = animals_list.filter(species=species)

    # Filter by size if provided
    size = request.GET.get('size')
    if size:
        animals_list = animals_list.filter(size=size)

    # Filter by age if provided
    age = request.GET.get('age')
    if age:
        animals_list = animals_list.filter(age_category=age)

    # Filter by rescue centre if provided
    rescue_centre = request.GET.get('rescue_centre')
    if rescue_centre:
        animals_list = animals_list.filter(rescue_centre_id=rescue_centre)

    # Pagination
    paginator = Paginator(animals_list, 12)  # Show 12 animals per page
    page = request.GET.get('page')
    try:
        animals = paginator.page(page)
    except PageNotAnInteger:
        animals = paginator.page(1)
    except EmptyPage:
        animals = paginator.page(paginator.num_pages)

    context = {
        'animals': animals,
        'species_choices': Animal.SPECIES_CHOICES,
        'size_choices': Animal.SIZE_CHOICES,
        'age_choices': Animal.AGE_CHOICES,
    }

    return render(request, 'marketplace/animal_list.html', context)