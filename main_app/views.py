from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import DogParks, Reviews, Pictures
from .forms import ReviewForm, ImageForm

def home(request):
    return render(request, 'home.html')

def parks_index(request):
    return render(request, 'parks/index.html', {
        'parks': DogParks.objects.all()
    })

@csrf_exempt
def save_dog_park(request):
    if request.method == 'POST':
        park_name = request.POST.get('park_name', '')
        park_address = request.POST.get('park_address', '')

        #Was able to make duplicates created a conditional to prevent
        existing_park = DogParks.objects.filter(name = park_name, address = park_address).first()
        if existing_park:
            return JsonResponse({'status': 'error', 'message': "Looks like this park has already been saved by another user, you can find it in the 'User Saved Parks' tab."})

        dog_park = DogParks(name = park_name, address = park_address)
        dog_park.save()

        return JsonResponse({'status': 'success'})
    
    return JsonResponse({'status': 'error'})

def parks_detail(request, park_id):
    park = DogParks.objects.get(id=park_id)
    return render(request, 'parks/details.html', { 'park': park })

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

def park_pictures(request, park_id):
    park = DogParks.objects.get(id=park_id)
    return render(request, 'parks/pictures.html', { 'park': park })

def add_photo(request, park_id):
    park = DogParks.objects.get(id=park_id)
    user = request.user
    form = ImageForm(request.POST, request.FILES)
    if request.method == 'POST':
        print(f"POST data: {request.POST}")
        print(f"FILES data: {request.FILES}")
        if form.is_valid():
            form.instance.user = user
            form.instance.park = park
            form.save()
            return redirect('user_profile')
        else:
            print("form is not valid")
            print(form.errors)
    else:
        form = ImageForm()
    return render(request, 'parks/addpicture.html', {'form': form, 'park': park})

def delete_picture(request, id):
    picture = Pictures.objects.get(id=id)
    picture.delete()
    return redirect('user_profile')

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

def user_profile(request):
    return render(request, 'user/profile.html')

def map(request):
    return render(request, 'map/index.html')