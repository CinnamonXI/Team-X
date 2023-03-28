from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Profile, Follower
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def profile(request):
    context = {
        'title': 'My Profile'
    }
    return render(request, 'user/index.html', context)

@login_required
def edit_profile(request):
    context = {
        'title': 'Edit Profile'
    }
    return render(request, 'user/edit-profile.html', context)

@login_required
def follow(request, username):
    user_to_follow = get_object_or_404(User, username=username, is_active=True)
    try:
        follower = Follower.objects.get(user_to=user_to_follow, user_from=request.user)
        messages.warning(request, f'You already follow {user_to_follow}.')
        return redirect('users:user_profile', username=username)
    except Follower.DoesNotExist:
        follower = Follower.objects.create(user_to=user_to_follow, user_from=request.user)
        follower.save()
        user_to_follow.profile.followers.add(follower)
        messages.success(request, f'Successfully followed {user_to_follow}.')
        return redirect('users:user_profile', username=username)

@login_required
def unfollow(request, username):
    user_to_unfollow = get_object_or_404(User, username=username, is_active=True)
    try:
        follower = Follower.objects.get(user_to=user_to_unfollow, user_from=request.user)
        follower.delete()
        user_to_unfollow.profile.followers.remove(follower)
        messages.success(request, f'Successfully unfollowed {user_to_unfollow}.')
        return redirect('users:user_profile', username=username)
    except Follower.DoesNotExist:
        messages.warning(request, f'You do not follow {user_to_unfollow}.')
        return redirect('users:user_profile', username=username)

@login_required
def user_profile(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    context = {
        'user': user,
        'title': f"{user}'s Profile",
    }
    return render(request, 'user/index.html', context)