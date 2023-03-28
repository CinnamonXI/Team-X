from . import views
from django.urls import path

app_name = 'api'
urlpatterns = [
    path('users/', views.get_users, name='get_users'),
]