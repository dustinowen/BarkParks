from django.db import models
from django.forms import ModelForm
from .models import Reviews, Pictures, DogParks
from django.contrib.auth.models import User

class ReviewForm(ModelForm):
  class Meta:
    model = Reviews
    fields = ['date', 'rating', 'review']

class ImageForm(ModelForm):
  class Meta:
    model = Pictures
    fields = ['user', 'park', 'image', 'description', 'date' ]

class AddParkForm(ModelForm):
   class Meta:
     model = DogParks
     fields = ['name', 'address', 'hours']
