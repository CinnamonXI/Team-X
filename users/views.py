from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Profile
# Create your views here.

def profile(request):
    context = {
        'title': 'My Profile'
    }
    return render(request, 'user/index.html', context)

def edit_profile(request):
    context = {
        'title': 'Edit Profile'
    }
    return render(request, 'user/edit-profile.html', context)