from . import views
from django.urls import path

app_name = 'users'
urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('profile/<str:username>/follow/', views.follow, name='follow'),
    path('profile/<str:username>/unfollow/', views.unfollow, name='unfollow'),
]
