from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact, Faq
from users.models import Team
# Create your views here.
def index(request):
    context = {
        'title': 'Homepage',
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        'title': 'About Us',
        'teams': Team.objects.filter(is_active=True)
    }
    return render(request, 'about.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone_number = request.POST['phone_number']
        message = request.POST['message']
        contact = Contact(name=name, email=email, subject=subject, message=message, phone_number=phone_number)
        contact.save()
        messages.success(request, 'Message submitted successfully.')
        # subject = f'Contact: {subject} - {name} - {email}'
        # send_mail(subject,message, email, ['o.jeff3.a@gmail.com',],fail_silently=False,)
        return redirect('index')

    context = {
        'title': 'Contact Us'
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

def faq(request):
    faqs = Faq.objects.all()
    context = {
        'title': 'Frequently Asked Questions',
        'faqs': faqs
    }
    return render(request, 'faq/index.html', context)
