from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Animal, Rescuecentre  # Keep original model name

def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'marketplace/animal_list.html', {'animals': animals})

def animal_detail(request, pk):  # Keep original parameter name
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'marketplace/animal_detail.html', {'animal': animal})

def centre_list(request):
    centres = Rescuecentre.objects.all()
    return render(request, 'marketplace/centre_list.html', {'centres': centres})

def centre_detail(request, pk):  # Keep original parameter name
    centre = get_object_or_404(Rescuecentre, pk=pk)
    return render(request, 'marketplace/centre_detail.html', {'centre': centre})

def search_results(request):
    """Handle search requests"""
    query = request.GET.get('q', '')
    species = request.GET.get('species', '')
    size = request.GET.get('size', '')
    age = request.GET.get('age', '')

    animals = Animal.objects.all()
    if query:
        animals = animals.filter(name__icontains=query) | animals.filter(breed__icontains=query)
    if species:
        animals = animals.filter(species=species)
    if size:
        animals = animals.filter(size=size)
    if age:
        animals = animals.filter(age_category=age)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_to_string('marketplace/search_results.html', {
            'animals': animals
        })
        return JsonResponse({'html': html})

    return render(request, 'marketplace/search_results.html', {
        'animals': animals,
        'query': query,
        'species': species,
        'size': size,
        'age': age
    })