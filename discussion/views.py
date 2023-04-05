from django.shortcuts import render

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

def polls(request):
    context = {
        'title': 'Polls'
    }
    return render(request, 'forum/polls.html', context)

def communities(request):
    context = {
        'title': 'Communities'
    }
    return render(request, 'forum/communities.html', context)
