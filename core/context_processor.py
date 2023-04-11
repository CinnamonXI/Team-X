from .models import Category, Tag
from resources.models import Document, Video, Article
from django.contrib.auth.models import User
from discussion.models import Question, Answer

def categories(request):
    # latest_post = []
    # latest_article = Article.objects.order_by('-created_at')[:2]
    # latest_video = Video.objects.order_by('-created_at')[:2]
    # latest_document = Document.objects.order_by('-created_at')[:2]
    # latest_post.append(latest_article)
    # latest_post.append(latest_video)
    # latest_post.append(latest_document)  

    return {
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
        'latest_post': Question.objects.order_by('-likes')[:5],
        'top_members': User.objects.all()[:4],
        'total_users': User.objects.all().count(),
        'total_questions': Question.objects.all().count(),
        'total_answers': Answer.objects.all().count(),
    }