from django.db import models
from django.forms import ModelForm
from .models import Reviews
from django.contrib.auth.models import User

class ReviewForm(ModelForm):
  class Meta:
    model = Reviews
    fields = ['date', 'rating', 'review']

class UserForm(ModelForm):
  pass

class UserCreationForm(ModelForm):
  pass