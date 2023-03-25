from django.shortcuts import render
from core.models import Category
from .models import Article, Video, Document
from django.shortcuts import get_object_or_404

# Create your views here.
def article(request, slug=None):
    category = None
    if not slug:
        articles = Article.objects.filter(is_published=True)
    else:
        category = get_object_or_404(Category, slug=slug)
        articles = Article.objects.filter(category=category, is_published=True)
    context = {
        'title': 'Resource Articles',
        'categories': Category.objects.all(),
        'articles': articles,
        'category': category,
        'r_articles': 'active',
    }
    return render(request, 'resources/index.html', context)

def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    context = {
        'title': article.title,
        'article': article,
        'categories': Category.objects.all(),
    }
    return render(request, 'resources/details.html', context)

def video(request, slug=None):
    category = None
    if not slug:
        videos = Video.objects.filter(is_published=True)
    else:
        category = get_object_or_404(Category, slug=slug)
        videos = Video.objects.filter(category=category, is_published=True)
    context = {
        'title': 'Resource Videos',
        'categories': Category.objects.all(),
        'videos': videos,
        'category': category,
        'r_videos': 'active',
    }
    return render(request, 'resources/videos.html', context)

def documents(request, slug=None):
    category = None
    if not slug:
        documents = Document.objects.filter(is_published=True)
    else:
        category = get_object_or_404(Category, slug=slug)
        documents = Document.objects.filter(category=category, is_published=True)
    context = {
        'title': 'Resource Documents',
        'categories': Category.objects.all(),
        'documents': documents,
        'category': category,
        'r_documents': 'active',
    }
    return render(request, 'resources/documents.html', context)