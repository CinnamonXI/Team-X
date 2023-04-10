from django.shortcuts import get_object_or_404, redirect, render
from .models import Community, Group, Question, Answer
from core.models import Tag, Category
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.
def questions(request):
    questions = Question.objects.all()
    unanswered_questions = []
    for question in questions:
        if question.answers.count() == 0:
            unanswered_questions.append(question)

    most_answered_questions = sorted(questions, key=lambda x: x.answers.count(), reverse=True)
    most_recent_questions = sorted(questions, key=lambda x: x.created_at, reverse=True)
    most_viewed_questions = sorted(questions, key=lambda x: x.views, reverse=True)
    context = {
        'title': 'Questions',
        'unanswered_questions': unanswered_questions,
        'most_answered_questions': most_answered_questions,
        'most_recent_questions': most_recent_questions,
        'most_viewed_questions': most_viewed_questions,
        'q_category': 'is_active',
    }
    return render(request, 'forum/index.html', context)

def question_detail(request, slug):
    question = get_object_or_404(Question, slug=slug)
    question.views += 1
    question.save()
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            answer = Answer.objects.create(
                content=content,
                user=request.user,
                question=question,
            )
            answer.save()
            messages.success(request, 'Your answer has been posted successfully')
            return redirect('questions:question_detail', slug=question.slug)
        else:
            messages.warning(request, 'An error occurred while posting your answer, please try again')
            return redirect('questions:question_detail', slug=question.slug)
        
    context = {
        'title': question.title,
        'question': question,
        'q_category': 'is_active',
    }
    return render(request, 'forum/question-details.html', context)

@login_required
def ask(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')
        tags = request.POST.getlist('tags')
        category = Category.objects.get(id=category)
        
        if title and description and category:
            question = Question.objects.create(
                title=title,
                description=description,
                user=request.user,
                slug=title.replace(' ', '-').lower(),
                category=category,
            )
            if tags:
                # Split the tags by comma and remove the spaces after the comma
                tags = [tag.strip() for tag in tags[0].split(',')]

                for tag in tags:
                    # Check if tag exists in the database, if not create it and not add it to the question and not case sensitive
                    if Tag.objects.filter(title__iexact=tag).exists():
                        tag = Tag.objects.get(title__iexact=tag)
                        question.tags.add(tag)
                    else:
                        tag = Tag.objects.create(title=tag, slug=tag.replace(' ', '-').lower())
                        tag.save()
                        question.tags.add(tag)

            question.save()
            messages.success(request, 'Your question has been posted successfully')
            return redirect('questions:question_detail', slug=question.slug)
        else:
            messages.warning(request, 'An error occurred while posting your question, please try again')
            return redirect('questions:ask')
        
    context = {
        'title': 'Ask Questions',
        'categories': Category.objects.all(),
        'q_category': 'is_active',
    }
    return render(request, 'forum/ask-questions.html', context)

# Groups
def group_list(request):
    context = {
        'title': 'Groups',
        'groups': Group.objects.all(),
        'category': 'groups',
        'q_category': 'is_active',
    }
    return render(request, 'forum/groups/index.html', context)

@login_required
def group_about(request, slug):
    group = get_object_or_404(Group, slug=slug)
    context = {
        'title': group.title,
        'group': group,
        'category': 'groups',
    }
    return render(request, 'forum/groups/details.html', context)

@login_required
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    if request.user in group.members.all():
        questions = Question.objects.filter(group=group)
    else:
        messages.warning(request, 'You are not a member of this group, please join the group to view the posts')
        return redirect('questions:groups')
    
    context = {
        'title': group.title,
        'group': group,
        'category': 'groups',
        'questions': questions,
    }
    return render(request, 'forum/groups/posts.html', context)

@login_required
def ask_group(request, slug):
    group = get_object_or_404(Group, slug=slug)
    if request.user in group.members.all():
        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            category = request.POST.get('category')
            tags = request.POST.getlist('tags')
            category = Category.objects.get(id=category)
            
            if title and description and category:
                question = Question.objects.create(
                    title=title,
                    description=description,
                    user=request.user,
                    slug=title.replace(' ', '-').lower(),
                    category=category,
                    group=group,
                )
                if tags:
                    # Split the tags by comma and remove the spaces after the comma
                    tags = [tag.strip() for tag in tags[0].split(',')]

                    for tag in tags:
                        # Check if tag exists in the database, if not create it and not add it to the question and not case sensitive
                        if Tag.objects.filter(title__iexact=tag).exists():
                            tag = Tag.objects.get(title__iexact=tag)
                            question.tags.add(tag)
                        else:
                            tag = Tag.objects.create(title=tag, slug=tag.replace(' ', '-').lower())
                            tag.save()
                            question.tags.add(tag)

                question.save()
                messages.success(request, f"Your question has been posted to group '{group.title}' successfully")
                return redirect('questions:group_detail', slug=group.slug)
            else:
                messages.warning(request, 'An error occurred while posting your question, please try again')
                return redirect('questions:ask_group', slug=group.slug)
    else:
        messages.warning(request, 'You are not a member of this group, please join the group to ask a question')
        return redirect('questions:groups')
        
    context = {
        'title': 'Ask Group',
        'category': 'groups',
        'group_slug': group.slug,
        'q_category': 'is_active',
    }
    return render(request, 'forum/ask-questions.html', context)

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
        'title': 'Tags',
        'q_category': 'is_active',
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
    return redirect('questions:tag_detail', slug=tag.slug)

@login_required
def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    questions = Question.objects.filter(tags=tag)
    
    context = {
        'title': tag.title,
        'tag': tag,
        'questions': questions,
    }
    return render(request, 'forum/tag-detail.html', context)

# Communities
def communities(request):
    context = {
        'title': 'Communities',
        'communities': Community.objects.all(),
        'q_category': 'is_active',
    }
    return render(request, 'forum/community/index.html', context)

@login_required
def community_about(request, slug):
    community = get_object_or_404(Community, slug=slug)
    context = {
        'title': community.title,
        'community': community,
        'category': 'community',
    }
    return render(request, 'forum/community/details.html', context)

@login_required
def community_posts(request, slug):
    community = get_object_or_404(Community, slug=slug)
    if request.user in community.followers.all():
        questions = Question.objects.filter(community=community)
    else:
        messages.warning(request, f"You are not following the community '{community.title}', follow it to see the posts in it")
        return redirect('questions:communities')
    
    context = {
        'title': community.title,
        'community': community,
        'category': 'community',
        'questions': questions,
    }
    return render(request, 'forum/community/posts.html', context)

@login_required
def ask_community(request, slug):
    community = get_object_or_404(Community, slug=slug)
    if request.user in community.followers.all():
        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            category = request.POST.get('category')
            tags = request.POST.getlist('tags')
            category = Category.objects.get(id=category)
            
            if title and description and category:
                question = Question.objects.create(
                    title=title,
                    description=description,
                    user=request.user,
                    slug=title.replace(' ', '-').lower(),
                    category=category,
                    community=community,
                )
                if tags:
                    # Split the tags by comma and remove the spaces after the comma
                    tags = [tag.strip() for tag in tags[0].split(',')]

                    for tag in tags:
                        # Check if tag exists in the database, if not create it and not add it to the question and not case sensitive
                        if Tag.objects.filter(title__iexact=tag).exists():
                            tag = Tag.objects.get(title__iexact=tag)
                            question.tags.add(tag)
                        else:
                            tag = Tag.objects.create(title=tag, slug=tag.replace(' ', '-').lower())
                            tag.save()
                            question.tags.add(tag)

                question.save()
                messages.success(request, f"Your question has been posted to community '{community.title}' successfully")
                return redirect('questions:community_detail', slug=community.slug)
            else:
                messages.warning(request, 'An error occurred while posting your question, please try again')
                return redirect('questions:ask_community', slug=community.slug)
    else:
        messages.warning(request, 'You are not following the community, please follow it to ask a question')
        return redirect('questions:communities')
    
    context = {
        'title': 'Ask Community',
        'category': 'community',
        'q_category': 'is_active',
    }
    return render(request, 'forum/ask-questions.html', context)

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

@login_required
def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    questions = Question.objects.filter(category=category)
    context = {
        'title': category.title,
        'questions': questions,
    }
    return render(request, 'forum/category-detail.html', context)

def search(request):
    query = request.GET.get('q')
    if query:
        questions = Question.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)| Q(tags__title__icontains=query))
        total_results = questions.count()
        unanswered_questions = []
        for question in questions:
            if question.answers.count() == 0:
                unanswered_questions.append(question)

        most_answered_questions = sorted(questions, key=lambda x: x.answers.count(), reverse=True)
        most_recent_questions = sorted(questions, key=lambda x: x.created_at, reverse=True)
        most_viewed_questions = sorted(questions, key=lambda x: x.views, reverse=True)

        context = {
            'title': f"({total_results})Search results for  '{query}'",
            'questions': questions,
            'q_category': 'is_active',
            'unanswered_questions': unanswered_questions,
            'most_answered_questions': most_answered_questions,
            'most_recent_questions': most_recent_questions,
            'most_viewed_questions': most_viewed_questions,
        }
        return render(request, 'forum/index.html', context)
    else:
        messages.warning(request, 'Please enter a search term')
        return redirect('questions:all')
    
