from django.forms import ModelForm
from .models import Reviews

class ReviewForm(ModelForm):
  class Meta:
    model = Reviews
    fields = ['date', 'rating', 'review']

class UserForm(ModelForm):
  pass