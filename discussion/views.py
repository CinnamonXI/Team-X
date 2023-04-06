from django.shortcuts import get_object_or_404, redirect, render
from .models import Community, Group, Question, Answer
from core.models import Tag
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def all_questions(request):
    all_questions = Question.objects.all()
    unanswered_questions = []
    for question in all_questions:
        if question.answers.count() == 0:
            unanswered_questions.append(question)

    most_answered_questions = sorted(all_questions, key=lambda x: x.answers.count(), reverse=True)
    most_recent_questions = sorted(all_questions, key=lambda x: x.created_at, reverse=True)
    context = {
        'title': 'All Questions',
        'category': 'Questions',
        'all_questions': all_questions,
        'unanswered_questions': unanswered_questions,
        'most_answered_questions': most_answered_questions,
        'most_recent_questions': most_recent_questions,
    }
    return render(request, 'forum/index.html', context)


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
        messages.success(request, f"You have left the group '{group.title}'")
    else:
        group.members.add(request.user)
        messages.success(request, f"You have joined the group '{group.title}'")
    return redirect('questions:group_detail', slug=group.slug)


# Tags
def tag_list(request):
    context = {
        'title': 'Tags'
    }
    return render(request, 'forum/tags.html', context)

@login_required
def follow_unfollow_tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    if request.user in tag.followers.all():
        tag.followers.remove(request.user)
        messages.success(request, f"You have unfollowed the tag '{tag.title}'")
    else:
        tag.followers.add(request.user)
        messages.success(request, f"You have followed the tag '{tag.title}'")
    return redirect('questions:tags')


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
            messages.success(request, f"You have unfollowed the community '{community.title}'")
        else:
            community.followers.add(request.user)
            messages.success(request, f"You have followed the community '{community.title}'")
    return redirect('questions:community_detail', slug=community.slug)


