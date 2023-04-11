from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact, Faq, Category, Tag
from users.models import Team
from resources.models import Article, Video, Document
from discussion.models import Question
# Create your views here.
def check_if_userprofile_is_updated(user):
    if user.first_name and user.last_name and user.email:
        return True
    else:
        return False

def index(request):
    questions = Question.objects.all()
    unanswered_questions = []
    for question in questions:
        if question.answers.count() == 0:
            unanswered_questions.append(question)

    most_answered_questions = sorted(questions, key=lambda x: x.answers.count(), reverse=True)
    most_recent_questions = sorted(questions, key=lambda x: x.created_at, reverse=True)
    most_viewed_questions = sorted(questions, key=lambda x: x.views, reverse=True)
    if request.user.is_authenticated and not check_if_userprofile_is_updated(request.user):
        messages.warning(request, 'Please update your profile to get the best experience.')
    context = {
        'title': 'Homepage',
        'unanswered_questions': unanswered_questions,
        'most_answered_questions': most_answered_questions,
        'most_recent_questions': most_recent_questions,
        'most_viewed_questions': most_viewed_questions,
        'q_category': 'is_active',
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

def faq(request, slug=None):
    category = None
    if not slug:
        faqs = Faq.objects.all()
    else:
        category = get_object_or_404(Category, slug=slug)
        faqs = Faq.objects.filter(category=category)
    
    context = {
        'title': 'Frequently Asked Questions',
        'faqs': faqs,
        'faq' : 'active',
        'categories' : Category.objects.all(),
    }
    return render(request, 'faq/index.html', context)

def search(request):
    try:
        if request.method == 'GET':
            search = request.GET.get('q')
            articles = Article.objects.filter(title__icontains=search) or Article.objects.filter(description__icontains=search)
            videos = Video.objects.filter(title__icontains=search) 
            documents = Document.objects.filter(title__icontains=search) 
            context = {
                'title': f"Search result for '{search}'",
                'articles': articles,
                'videos': videos,
                'documents': documents,
            }
            return render(request, 'index.html', context)
    except ValueError:
        return redirect('index')