from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Homepage',
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        'title': 'About Us',
    }
    return render(request, 'about.html', context)

def contact(request):
    context = {
        'title': 'Contact Us',
    }
    return render(request, 'contact.html', context)

def terms(request):
    context = {
        'title': 'Terms and Conditions',
    }
    return render(request, 'terms.html', context)

def privacy(request):
    context = {
        'title': 'Privacy Policy',
    }
    return render(request, 'privacy.html', context)

def help(request):
    context = {
        'title': 'Help Page',
    }
    return render(request, 'help.html', context)

def faq(request):
    context = {
        'title': 'Frequently Asked Questions',
    }
    return render(request, 'faq/index.html', context)

def ar(request):
    context = {
        'title': 'Test Page',
    }
    return render(request, 'resources/index.html', context)