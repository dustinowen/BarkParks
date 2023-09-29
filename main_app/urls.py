from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),

    path('parks/', views.parks_index, name='parksindex'),

    path('parks/<int:park_id>/', views.parks_detail, name="park_details"),

    path('parks/<int:park_id>/pictures', views.park_pictures, name="park_pictures"),

    path('park/<int:park_id>/addreview/', views.add_review, name="addreview"),

    path('park/<int:park_id>/postreview/', views.post_review, name="postreview"),

    path('user/', views.user_profile, name='user_profile'),

    path('user/login/', views.user_login, name='user_login'),

    path('user/signup/', views.user_signup, name='user_signup'),

    path('user/favorites/', views.favorites, name='favorites'),

    path('map/', views.map, name='map'),\
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)