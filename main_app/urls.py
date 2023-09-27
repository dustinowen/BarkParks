from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('parks/', views.parks_index, name='parksindex'),
    path('parks/<int:park_id>/', views.parks_detail, name="park_details"),
]