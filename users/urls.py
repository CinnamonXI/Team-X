from . import views
from django.urls import path

app_name = 'users'
urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('health-records/', views.user_health_records, name='health_records'),
    path('health-records/add/', views.add_health_record, name='add_health_record'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('profile/<str:username>/follow/', views.follow, name='follow'),
    path('profile/<str:username>/unfollow/', views.unfollow, name='unfollow'),
    path('health-records/<int:id>/edit/', views.edit_health_record, name='edit_health_record'),
    path('health-records/<int:id>/delete/', views.delete_health_record, name='delete_health_record'),
]
