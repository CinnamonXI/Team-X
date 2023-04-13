from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Profile, Follower, HealthData
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from core.views import check_if_userprofile_is_updated
import re
# Create your views here.

def validate_username(username):
    regex = '^[a-zA-Z0-9]+$'
    if not re.match(regex, username):
        return False
    return True

def get_following(user):
    following = Follower.objects.filter(user_from=user)
    return following

@login_required
def profile(request):
    if request.user.is_authenticated and not check_if_userprofile_is_updated(request.user):
        messages.warning(request, 'Please update your profile to get the best experience.')
    context = {
        'title': 'My Profile',
        'total_followers': get_following(request.user).count(),
    }
    return render(request, 'user/index.html', context)

@login_required
def edit_profile(request): 
    user = request.user
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        location = request.POST.get('location')
        phone_number = request.POST.get('phone_number')
        language_preference = request.POST.get('language_preference')
        instagram = request.POST.get('instagram')
        twitter = request.POST.get('twitter')
        linkedin = request.POST.get('linkedin')
        image = request.FILES.get('image', None)
        # print(username)
        #validate username to confirm it doesnt contain spaces and special characters
        if not validate_username(username):
            messages.warning(request, 'Username can only contain letters and numbers.')
            return redirect('users:edit_profile')
        else:
            #validate username to confirm it doesnt already exist
            if User.objects.filter(username=username).exists() and username != user.username:
                messages.warning(request, 'Username already exists.')
                return redirect('users:edit_profile')
            else:
                user.username = username
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.save()
                profile = Profile.objects.get(user=user)
                profile.bio = bio
                profile.phone_number = phone_number
                profile.gender = gender
                profile.age = age
                profile.location = location
                profile.language_preference = language_preference
                profile.instagram = instagram
                profile.twitter = twitter
                profile.linkedin = linkedin
                if image:
                    profile.image = image
                profile.save()
                messages.success(request, 'Profile updated successfully.')        

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
    try:
        follower = Follower.objects.get(user_to=user, user_from=request.user)
        is_following = True
    except Follower.DoesNotExist:
        is_following = False
    context = {
        'user': user,
        'title': f"{user}'s Profile",
        'is_following': is_following,
        'total_followers': get_following(user).count(), 
    }
    return render(request, 'user/index.html', context)

@login_required
def user_health_records(request):
    health_data = HealthData.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'title': f"{request.user}'s Health Records",
        'health_records': health_data
    }
    return render(request, 'user/health_records/index.html', context)

@login_required
def add_health_record(request):

    if request.method == 'POST':
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        heart_rate = request.POST.get('heart_rate')
        systolic_bp = request.POST.get('systolic_bp')
        diastolic_bp = request.POST.get('diastolic_bp')
        interest = request.POST.get('interest')
        allergies = request.POST.get('allergies')
        status = request.POST.get('status')
        is_disabled = request.POST.get('is_disabled')
        smoke = request.POST.get('smoke')
        take_alcohol = request.POST.get('take_alcohol')
        #convert to boolean
        if is_disabled == 'True':
                is_disabled = True
        else:
            is_disabled = False
        if smoke == 'True':
            smoke = True
        else:
            smoke = False
        if take_alcohol == 'True':
            take_alcohol = True
        else:
            take_alcohol = False

        health_data = HealthData.objects.create(
            user=request.user,
            weight=weight,
            height=height,
            heart_rate=heart_rate,
            systolic_bp=systolic_bp,
            diastolic_bp=diastolic_bp,
            interests=interest,
            allergies=allergies,
            status=status,
            take_alcohol = take_alcohol,
            smoke = smoke,
            is_disabled = is_disabled
        )
        health_data.save()
        messages.success(request, 'Health record added successfully.')
        return redirect('users:health_records')

    context = {
        'title': 'Add Health Record'
    }
    return render(request, 'user/health_records/add.html', context)

@login_required
def edit_health_record(request, id):
    health_data = get_object_or_404(HealthData, id=id)
    if request.user != health_data.user:
        messages.warning(request, 'You are not authorized to edit this health record.')
        return redirect('users:health_records')
    else:
        if request.method == 'POST':
            weight = request.POST.get('weight')
            height = request.POST.get('height')
            heart_rate = request.POST.get('heart_rate')
            systolic_bp = request.POST.get('systolic_bp')
            diastolic_bp = request.POST.get('diastolic_bp')
            interest = request.POST.get('interest')
            allergies = request.POST.get('allergies')
            status = request.POST.get('status')
            is_disabled = request.POST.get('is_disabled')
            smoke = request.POST.get('smoke')
            take_alcohol = request.POST.get('take_alcohol')
            #convert to boolean
            if is_disabled == 'True':
                is_disabled = True
            else:
                is_disabled = False
            if smoke == 'True':
                smoke = True
            else:
                smoke = False
            if take_alcohol == 'True':
                take_alcohol = True
            else:
                take_alcohol = False

            health_data.weight = weight
            health_data.height = height
            health_data.heart_rate = heart_rate
            health_data.systolic_bp = systolic_bp
            health_data.diastolic_bp = diastolic_bp
            health_data.interests = interest
            health_data.allergies = allergies
            health_data.status = status
            health_data.take_alcohol = take_alcohol
            health_data.smoke = smoke
            health_data.is_disabled = is_disabled
            health_data.save()
            messages.success(request, 'Health record updated successfully.')
            return redirect('users:health_records')

        context = {
            'title': 'Edit Health Record',
            'record': health_data
        }
        return render(request, 'user/health_records/edit.html', context)

@login_required
def delete_health_record(request, id):
    health_data = get_object_or_404(HealthData, id=id)
    if request.user != health_data.user:
        messages.warning(request, 'You are not authorized to delete this health record.')
        return redirect('users:health_records')
    else:
        health_data.delete()
        messages.success(request, 'Health record deleted successfully.')
        return redirect('users:health_records')
    
def referal(request):
    context ={
        'title': 'Referrals'
    }
    return render(request, 'user/referrals.html', context)

def users(request):
    users = User.objects.all()
    is_following = False
    for user in users:
        try:
            follower = Follower.objects.get(user_to=user, user_from=request.user)
            is_following = True
        except Follower.DoesNotExist:
            is_following = False

    context = {
        'title': 'Users',
         'is_following': is_following,
        'users': users,
    }
    return render(request, 'user/users.html', context)