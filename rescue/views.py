from django.shortcuts import render, get_object_or_404
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