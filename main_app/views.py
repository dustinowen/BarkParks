from django.shortcuts import render, redirect
from .models import DogParks
from .forms import ReviewForm


def home(request):
    return render(request, 'home.html')

def parks_index(request):
    return render(request, 'parks/index.html', {
        'parks': DogParks.objects.all()
    })

def parks_detail(request, park_id):
    park = DogParks.objects.get(id=park_id)
    return render(request, 'parks/details.html', { 'park': park})

def add_review(request, park_id):
    park= DogParks.objects.get(id=park_id)
    review_form = ReviewForm()
    return render(request, 'parks/addreview.html', {'park': park, 'review_form': review_form })

def post_review(request, park_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.park_id = park_id
        new_review.save()
    return redirect('park_details', park_id=park_id)

def map(request):
    return render(request, 'map/index.html')

def favorites(request):
    return render(request, 'user/favorites.html')


def user_profile(request):
    return render(request, 'user/profile.html')