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


# Groups
def group_list(request):
    context = {
        'title': 'Groups',
        'groups': Group.objects.all(),
        'category': 'groups',
    }
    return render(request, 'forum/groups/index.html', context)
@login_required
def group_detail(request, slug):
    group = get_object_or_404(Group, slug=slug)
    context = {
        'title': group.title,
        'group': group,
        'category': 'groups',
    }
    return render(request, 'forum/groups/details.html', context)
@login_required
def join_leave_group(request, slug):
    group = get_object_or_404(Group, slug=slug)
    if request.user in group.members.all():
        group.members.remove(request.user)
        messages.success(request, 'You have left the group')
    else:
        group.members.add(request.user)
        messages.success(request, 'You have joined the group')
    return redirect('questions:group_detail', slug=group.slug)

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

# Communities
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
            messages.success(request, 'You have unfollowed the community')
        else:
            community.followers.add(request.user)
            messages.success(request, 'You have followed the community')
    return redirect('questions:community_detail', slug=community.slug)


