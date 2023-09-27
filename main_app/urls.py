from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('parks/', views.parks_index, name='parksindex'),


    path('parks/<int:park_id>/', views.parks_detail, name="park_details"),

    path('park/<int:park_id>/addreview/', views.add_review, name="addreview"),

    path('park/<int:park_id>/postreview/', views.post_review, name="postreview"),

    path('user/', views.user_profile, name='user_profile'),

    path('user/favorites/', views.favorites, name='favorites'),

    path('map/', views.map, name='map'),
]
