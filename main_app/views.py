from django.shortcuts import render
from .models import DogParks


def home(request):
    return render(request, 'home.html')

def parks_index(request):
    return render(request, 'parks/index.html', {
        'parks': DogParks.objects.all()
    })

def parks_detail(request, park_id):
    park = DogParks.objects.get(id=park_id)
    return render(request, 'parks/details.html', { 'park': park })