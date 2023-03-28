from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
# Create your views here.
def get_users(request):
    users = []
    for user in User.objects.all():
        users.append({
            'new data': user.username,
        })

    return JsonResponse(users, safe=False)