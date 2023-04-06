from django.shortcuts import get_object_or_404, redirect, render
from .models import Community, Group, Question, Answer
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def all_questions(request):
    context = {
        'title': 'All Questions',
        'category': 'Questions',
    }
    return render(request, 'forum/all-questions.html', context)

def unanswered(request):
    context = {
        'title': 'Unanswered',
        'category': 'Questions',
    }
    return render(request, 'forum/unanswered.html', context)

def most_answered(request):
    context = {
        'title': 'Most Answered',
        'category': 'Questions',
    }
    return render(request, 'forum/most-answered.html', context)

def most_recent(request):
    context = {
        'title': 'Most Recent',
        'category': 'Questions',
    }
    return render(request, 'forum/all-questions.html', context)

def ask(request):
    context = {
        'title': 'Ask Questions'
    }
    return render(request, 'forum/ask-questions.html', context)

def group_list(request):
    context = {
        'title': 'Groups'
    }
    return render(request, 'forum/groups.html', context)

def tag_list(request):
    context = {
        'title': 'Tags'
    }
    return render(request, 'forum/tags.html', context)

def badge_list(request):
    context = {
        'title': 'Badges'
    }
    return render(request, 'forum/badges.html', context)

def communities(request):
    context = {
        'title': 'Communities',
        'communities': Community.objects.all(),
    }
    return render(request, 'forum/community/index.html', context)

@login_required
def community_detail(request, slug):
    community = get_object_or_404(Community, slug=slug)
    context = {
        'title': community.title,
        'community': community,
        'category': 'community',
    }
    return render(request, 'forum/community/details.html', context)

@login_required
def follow_unfollow_community(request, slug):
    community = get_object_or_404(Community, slug=slug)
    if request.user.is_authenticated:
        if request.user in community.followers.all():
            community.followers.remove(request.user)
        else:
            community.followers.add(request.user)
    return redirect('questions:community_detail', slug=community.slug)


