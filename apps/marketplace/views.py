from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Animal, RescueCentre, Contact
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def animal_list(request):
    """Browse all animals - no search filters applied by default"""
    animals_list = Animal.objects.filter(is_available=True)

    # Basic filters for browsing
    selected_species = request.GET.getlist('species')
    if selected_species:
        animals_list = animals_list.filter(species__in=selected_species)

    size = request.GET.get('size')
    if size:
        animals_list = animals_list.filter(size=size)

    age = request.GET.get('age')
    if age:
        animals_list = animals_list.filter(age_category=age)

    # Pagination
    paginator = Paginator(animals_list, 12)
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
        'gender_choices': Animal.GENDER_CHOICES,
        'selected_species': selected_species,

}
    print("Selected species:", selected_species)
    print("All GET data:", request.GET)
    return render(request, 'marketplace/animal_list.html', context)

def search_results(request):
    """Advanced search results with all filters - matches your model exactly"""
    animals_list = Animal.objects.filter(is_available=True)

    # Text search
    query = request.GET.get('q', '')
    if query:
        animals_list = animals_list.filter(
            Q(name__icontains=query) | 
            Q(breed__icontains=query) | 
            Q(description__icontains=query)
        )

    # Species filter (can be multiple)
    species = request.GET.getlist('species')
    if species:
        animals_list = animals_list.filter(species__in=species)
        
        # Handle subspecies based on main species
        for sp in species:
            if sp == 'SMALL_ANIMAL':
                small_animal_type = request.GET.get('small_animal_type')
                if small_animal_type:
                    animals_list = animals_list.filter(small_animal_type=small_animal_type)
            elif sp == 'BIRD':
                bird_type = request.GET.get('bird_type')
                if bird_type:
                    animals_list = animals_list.filter(bird_type=bird_type)
            elif sp == 'REPTILE':
                reptile_type = request.GET.get('reptile_type')
                if reptile_type:
                    animals_list = animals_list.filter(reptile_type=reptile_type)

    # Basic filters
    breed = request.GET.get('breed')
    if breed:
        animals_list = animals_list.filter(breed__icontains=breed)

    gender = request.GET.get('gender')
    if gender:
        animals_list = animals_list.filter(gender=gender)

    age = request.GET.get('age')
    if age:
        animals_list = animals_list.filter(age_category=age)

    size = request.GET.get('size')
    if size:
        animals_list = animals_list.filter(size=size)

    # Appearance filters
    colour = request.GET.get('colour')
    if colour:
        animals_list = animals_list.filter(colour__icontains=colour)

    coat_length = request.GET.get('coat_length')
    if coat_length:
        animals_list = animals_list.filter(coat_length=coat_length)

    # Behavior filters
    temperament = request.GET.get('temperament')
    if temperament:
        animals_list = animals_list.filter(temperament__icontains=temperament)

    good_with = request.GET.get('good_with')
    if good_with:
        animals_list = animals_list.filter(good_with__icontains=good_with)

    energy_level = request.GET.get('energy_level')
    if energy_level:
        animals_list = animals_list.filter(energy_level=energy_level)

    training_level = request.GET.get('training_level')
    if training_level:
        animals_list = animals_list.filter(training_level=training_level)

    # Status filters - ✅ USING CORRECT MODEL FIELDS
    urgent = request.GET.get('urgent')
    if urgent == 'on':
        animals_list = animals_list.filter(urgent=True)  # ✅ Boolean field exists

    long_stay = request.GET.get('long_stay')
    if long_stay == 'on':
        animals_list = animals_list.filter(long_stay=True)  # ✅ Boolean field exists

    new_arrival = request.GET.get('new_arrival')
    if new_arrival == 'on':
        animals_list = animals_list.filter(new_arrival=True)  # ✅ Boolean field exists

    special_needs_flag = request.GET.get('special_needs_flag')
    if special_needs_flag == 'on':
        animals_list = animals_list.filter(special_needs_flag=True)  # ✅ Boolean field exists

    # Urgency status filter
    urgency_status = request.GET.get('urgency_status')
    if urgency_status:
        animals_list = animals_list.filter(urgency_status=urgency_status)

    # Foster status filter
    foster_status = request.GET.get('foster_status')
    if foster_status:
        animals_list = animals_list.filter(foster_status=foster_status)

   # Location filter - ✅ IMPROVED LOCATION SEARCH
    location = request.GET.get('location')
    if location:
        animals_list = animals_list.filter(
            Q(location__icontains=location) | 
            Q(postcode__icontains=location) |
            Q(rescue_centre__name__icontains=location) |
            Q(rescue_centre__address__icontains=location) |
            Q(rescue_centre__postcode__icontains=location)
        )

    postcode = request.GET.get('postcode')
    if postcode:
        animals_list = animals_list.filter(
            Q(postcode__icontains=postcode) |
            Q(rescue_centre__postcode__icontains=postcode)
        )
        
    # Rescue centre filter
    rescue_centre = request.GET.get('rescue_centre')
    if rescue_centre:
        animals_list = animals_list.filter(rescue_centre_id=rescue_centre)

    # Background filter
    background = request.GET.get('background')
    if background:
        animals_list = animals_list.filter(background__icontains=background)

    # Date filters - ✅ USING CORRECT FIELD NAMES
    date_added_from = request.GET.get('date_added_from')
    if date_added_from:
        animals_list = animals_list.filter(date_added__gte=date_added_from)  # ✅ date_added exists

    date_added_to = request.GET.get('date_added_to')
    if date_added_to:
        animals_list = animals_list.filter(date_added__lte=date_added_to)  # ✅ date_added exists

    # Adoption details filters
    adoption_fee = request.GET.get('adoption_fee')
    if adoption_fee:
        animals_list = animals_list.filter(adoption_fee=adoption_fee)

    home_check = request.GET.get('home_check')
    if home_check:
        animals_list = animals_list.filter(home_check=home_check)

    transport_available = request.GET.get('transport_available')
    if transport_available:
        animals_list = animals_list.filter(transport_available=transport_available)

    # Pagination
    paginator = Paginator(animals_list, 12)
    page = request.GET.get('page')
    try:
        animals = paginator.page(page)
    except PageNotAnInteger:
        animals = paginator.page(1)
    except EmptyPage:
        animals = paginator.page(paginator.num_pages)

    context = {
        'animals': animals,
        'query': query,
        'species_choices': Animal.SPECIES_CHOICES,
        'size_choices': Animal.SIZE_CHOICES,
        'age_choices': Animal.AGE_CHOICES,
        'gender_choices': Animal.GENDER_CHOICES,
        'coat_length_choices': Animal.COAT_LENGTH_CHOICES,
        'energy_level_choices': Animal.ENERGY_LEVEL,
        'training_level_choices': Animal.TRAINING_LEVEL,
        'urgency_status_choices': Animal.URGENCY_STATUS,
        'foster_status_choices': Animal.FOSTER_STATUS,
        'adoption_fee_choices': Animal.ADOPTION_FEE_RANGES,
        'home_check_choices': Animal.HOME_CHECK_STATUS,
        'transport_choices': Animal.TRANSPORT_OPTIONS,
        'small_animal_types': Animal.SMALL_ANIMAL_TYPES,
        'bird_types': Animal.BIRD_TYPES,
        'reptile_types': Animal.REPTILE_TYPES,
    }
    return render(request, 'marketplace/search_results.html', context)

def animal_search_form(request):
    """Redirect to search_results - this view should not be used anymore"""
    return redirect('marketplace:search_results')

def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    related_animals = Animal.objects.filter(
        species=animal.species,
        is_available=True
    ).exclude(pk=animal.pk)[:4]

    user_favourites = []
    if request.user.is_authenticated:
        try:
            from accounts.models import Favourite
            user_favourites = [fav.animal for fav in Favourite.objects.filter(user=request.user)]
        except ImportError:
            # Favourite model doesn't exist yet
            pass

    context = {
        'animal': animal,
        'related_animals': related_animals,
        'user_favourites': user_favourites,
    }
    return render(request, 'marketplace/animal_detail.html', context)

def animal_quick_view(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'marketplace/animal_quick_view.html', {'animal': animal})

def centre_list(request):
    centres_list = RescueCentre.objects.all()

    rescue_type = request.GET.get('rescue_type')
    if rescue_type:
        centres_list = centres_list.filter(rescue_type=rescue_type)

    services = request.GET.get('services')
    if services:
        centres_list = centres_list.filter(services=services)  # ✅ Exact match for choice field

    search = request.GET.get('search')
    if search:
        centres_list = centres_list.filter(
            Q(name__icontains=search) |
            Q(address__icontains=search) |
            Q(postcode__icontains=search)
        )

    sort = request.GET.get('sort')
    if sort:
        centres_list = centres_list.order_by(sort)

    # Count by rescue type - ✅ USING CORRECT CHOICE VALUES
    all_count = RescueCentre.objects.filter(rescue_type='ALL').count()
    dog_count = RescueCentre.objects.filter(rescue_type='DOG').count()
    cat_count = RescueCentre.objects.filter(rescue_type='CAT').count()
    horse_count = RescueCentre.objects.filter(rescue_type='HORSE').count()
    exotic_count = RescueCentre.objects.filter(rescue_type='EXOTIC').count()
    wildlife_count = RescueCentre.objects.filter(rescue_type='WILDLIFE').count()

    paginator = Paginator(centres_list, 10)
    page = request.GET.get('page')
    try:
        centres = paginator.page(page)
    except PageNotAnInteger:
        centres = paginator.page(1)
    except EmptyPage:
        centres = paginator.page(paginator.num_pages)

    context = {
        'centres': centres,
        'all_count': all_count,
        'dog_count': dog_count,
        'cat_count': cat_count,
        'horse_count': horse_count,
        'exotic_count': exotic_count,
        'wildlife_count': wildlife_count,
        'rescue_type_choices': RescueCentre.RESCUE_TYPE,
        'services_choices': RescueCentre.SERVICES_OFFERED,
    }
    return render(request, 'marketplace/centre_list.html', context)

def centre_detail(request, pk):
    centre = get_object_or_404(RescueCentre, pk=pk)
    animals_list = Animal.objects.filter(rescue_centre=centre, is_available=True)
    paginator = Paginator(animals_list, 9)
    page = request.GET.get('page')
    try:
        animals = paginator.page(page)
    except PageNotAnInteger:
        animals = paginator.page(1)
    except EmptyPage:
        animals = paginator.page(paginator.num_pages)

    context = {
        'centre': centre,
        'animals': animals,
    }
    return render(request, 'marketplace/centre_detail.html', context)

def centre_search_form(request):
    """Search results for rescue centres"""
    centres_list = RescueCentre.objects.all()
    
    rescue_type = request.GET.get('rescue_type')
    if rescue_type:
        centres_list = centres_list.filter(rescue_type=rescue_type)
        
    address = request.GET.get('address')
    if address:
        centres_list = centres_list.filter(address__icontains=address)
        
    postcode = request.GET.get('postcode')
    if postcode:
        centres_list = centres_list.filter(postcode__icontains=postcode)
        
    services = request.GET.get('services')
    if services:
        centres_list = centres_list.filter(services=services)  # ✅ Exact match
        
    name = request.GET.get('name')
    if name:
        centres_list = centres_list.filter(name__icontains=name)

    # Additional filters based on your model
    facilities = request.GET.get('facilities')
    if facilities:
        centres_list = centres_list.filter(facilities=facilities)

    transport_radius = request.GET.get('transport_radius')
    if transport_radius:
        centres_list = centres_list.filter(transport_radius=transport_radius)

    foster_network = request.GET.get('foster_network')
    if foster_network:
        centres_list = centres_list.filter(foster_network=foster_network)

    emergency_intake = request.GET.get('emergency_intake')
    if emergency_intake:
        centres_list = centres_list.filter(emergency_intake=emergency_intake)

    paginator = Paginator(centres_list, 10)
    page = request.GET.get('page')
    try:
        centres = paginator.page(page)
    except PageNotAnInteger:
        centres = paginator.page(1)
    except EmptyPage:
        centres = paginator.page(paginator.num_pages)

    context = {
        'centres': centres,
        'rescue_type_choices': RescueCentre.RESCUE_TYPE,
        'services_choices': RescueCentre.SERVICES_OFFERED,
        'facilities_choices': RescueCentre.FACILITIES,
        'transport_radius_choices': RescueCentre.TRANSPORT_RADIUS,
        'foster_network_choices': RescueCentre.FOSTER_NETWORK,
        'emergency_intake_choices': RescueCentre.EMERGENCY_INTAKE,
    }
    return render(request, 'marketplace/centre_list.html', context)

def search_autocomplete(request):
    query = request.GET.get('q', '')
    suggestions = []

    if query and len(query) >= 2:
        animal_name_suggestions = Animal.objects.filter(
            name__icontains=query,
            is_available=True
        ).values_list('name', flat=True)[:5]

        breed_suggestions = Animal.objects.filter(
            breed__icontains=query,
            is_available=True
        ).values_list('breed', flat=True).distinct()[:5]

        rescue_centre_suggestions = RescueCentre.objects.filter(
            name__icontains=query
        ).values_list('name', flat=True)[:3]

        suggestions = list(animal_name_suggestions)
        for breed in breed_suggestions:
            if breed not in suggestions:
                suggestions.append(f"{breed}")
        for centre in rescue_centre_suggestions:
            suggestions.append(f"Rescue Centre: {centre}")

    return JsonResponse({'suggestions': suggestions})