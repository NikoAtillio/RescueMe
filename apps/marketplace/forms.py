from django import forms
from .models import Animal, RescueCentre

class AnimalSearchForm(forms.Form):
    q = forms.CharField(
        required=False,
        label='Search',
        widget=forms.TextInput(attrs={'placeholder': 'Search animals...'})
    )
    species = forms.ChoiceField(
        required=False,
        choices=[('', 'All Species')] + list(Animal.SPECIES_CHOICES)
    )
    small_animal_type = forms.ChoiceField(
        required=False,
        choices=[('', 'All Small Animals')] + list(Animal.SMALL_ANIMAL_TYPES),
        label='Small Animal Type'
    )
    bird_type = forms.ChoiceField(
        required=False,
        choices=[('', 'All Birds')] + list(Animal.BIRD_TYPES),
        label='Bird Type'
    )
    reptile_type = forms.ChoiceField(
        required=False,
        choices=[('', 'All Reptiles')] + list(Animal.REPTILE_TYPES),
        label='Reptile Type'
    )
    size = forms.ChoiceField(
        required=False,
        choices=[('', 'All Sizes')] + list(Animal.SIZE_CHOICES)
    )
    age = forms.ChoiceField(
        required=False,
        choices=[('', 'All Ages')] + list(Animal.AGE_CHOICES)
    )
    breed = forms.CharField(
        required=False,
        label='Breed'
    )
    gender = forms.ChoiceField(
        required=False,
        choices=[('', 'Any Gender')] + list(Animal.GENDER_CHOICES)
    )
    colour = forms.CharField(
        required=False,
        label='Colour'
    )
    coat_length = forms.ChoiceField(
        required=False,
        choices=[('', 'Any Coat Length')] + list(Animal.COAT_LENGTH_CHOICES)
    )
    temperament = forms.CharField(
        required=False,
        label='Temperament'
    )
    good_with = forms.CharField(
        required=False,
        label='Good With'
    )
    urgent = forms.BooleanField(
        required=False,
        label='Urgent'
    )
    long_stay = forms.BooleanField(
        required=False,
        label='Long Stay'
    )
    new_arrival = forms.BooleanField(
        required=False,
        label='New Arrival'
    )
    special_needs_flag = forms.BooleanField(
        required=False,
        label='Special Needs'
    )
    location = forms.CharField(
        required=False,
        label='Location'
    )
    background = forms.CharField(
        required=False,
        label='Background'
    )
    date_added_from = forms.DateField(
        required=False,
        label='Added After',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    date_added_to = forms.DateField(
        required=False,
        label='Added Before',
        widget=forms.DateInput(attrs={'type': 'date'})
    )

class CentreSearchForm(forms.Form):
    search = forms.CharField(
        required=False, 
        label='Search',
        widget=forms.TextInput(attrs={'placeholder': 'Search centres...'})
    )
    rescue_type = forms.ChoiceField(
        required=False, 
        choices=[('', 'All Types')] + list(RescueCentre.RESCUE_TYPE)
    )
    services = forms.ChoiceField(
        required=False, 
        choices=[('', 'All Services')] + list(RescueCentre.SERVICES_OFFERED)
    )
    address = forms.CharField(required=False, label='Address')
    postcode = forms.CharField(required=False, label='Postcode')

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=False)
    subject = forms.CharField(max_length=200, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class AnimalInquiryForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=False)
    message = forms.CharField(widget=forms.Textarea, required=True)