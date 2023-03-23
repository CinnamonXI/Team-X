from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Home Page',
    }
    return render(request, 'base.html', context)

def about(request):
    context = {
        'title': 'About Us Page',
    }
    return render(request, 'base.html', context)

def contact(request):
    context = {
        'title': 'Contact Us Page',
    }
    return render(request, 'base.html', context)