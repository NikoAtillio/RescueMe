from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Animal, RescueCenter, Contact

def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'rescue/animal_list.html', {'animals': animals})

def center_list(request):
    centers = RescueCenter.objects.all()
    return render(request, 'rescue/center_list.html', {'centers': centers})

def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'rescue/animal_detail.html', {'animal': animal})

def center_detail(request, pk):
    center = get_object_or_404(RescueCenter, pk=pk)
    return render(request, 'rescue/center_detail.html', {'center': center})

def search_view(request):
    """Main search page view"""
    context = {
        'title': 'Search | Rescue Me',
    }
    return render(request, 'rescue/search.html', context)

def search_results(request):
    """Handle AJAX search requests"""
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

    html = render_to_string('rescue/search_results.html', {
        'animals': animals
    })

    return JsonResponse({'html': html})