from django import forms
from .models import Animal, RescueCentre

class AnimalSearchForm(forms.Form):
    q = forms.CharField(required=False, label='Search', 
                        widget=forms.TextInput(attrs={'placeholder': 'Search animals...'}))
    species = forms.ChoiceField(required=False, choices=[('', 'All Species')] + list(Animal.SPECIES_CHOICES))
    size = forms.ChoiceField(required=False, choices=[('', 'All Sizes')] + list(Animal.SIZE_CHOICES))
    age = forms.ChoiceField(required=False, choices=[('', 'All Ages')] + list(Animal.AGE_CHOICES))

class CentreSearchForm(forms.Form):
    search = forms.CharField(required=False, label='Search', 
                           widget=forms.TextInput(attrs={'placeholder': 'Search centres...'}))
    rescue_type = forms.ChoiceField(required=False, choices=[('', 'All Types')] + list(RescueCentre.RESCUE_TYPE))
    services = forms.ChoiceField(required=False, choices=[('', 'All Services')] + list(RescueCentre.SERVICES_OFFERED))

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