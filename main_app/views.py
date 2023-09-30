from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .models import DogParks, Reviews
from .forms import ReviewForm, ImageForm

def home(request):
    return render(request, 'home.html')

def parks_index(request):
    return render(request, 'parks/index.html', {
        'parks': DogParks.objects.all()
    })

def parks_detail(request, park_id):
    park = DogParks.objects.get(id=park_id)
    return render(request, 'parks/details.html', { 'park': park })

def park_pictures(request, park_id):
    park = DogParks.objects.get(id=park_id)
    return render(request, 'parks/pictures.html', { 'park': park })

def user_signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm
    return render(request, 'registration/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect (request.POST.get('next'))
            else:
                return redirect('user_profile')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', { 'form': form })

def add_review(request, park_id):
    park= DogParks.objects.get(id=park_id)
    review_form = ReviewForm()
    return render(request, 'parks/addreview.html', {'park': park, 'review_form': review_form })

def post_review(request, park_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.park_id = park_id
        new_review.user = request.user
        new_review.save()
    return redirect('park_details', park_id=park_id)

def delete_review(request, id):
    review = Reviews.objects.get(id=id)
    review.delete()
    return redirect('user_profile')

def map(request):
    return render(request, 'map/index.html')

def favorites(request):
    return render(request, 'user/favorites.html')

def user_profile(request):
    return render(request, 'user/profile.html')

def upload_photo(request):
    form = ImageForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('user_profile')
        else:
            form = ImageForm()
    return render(request, 'parks/addpicture.html', {'form': form})