from .models import Category, Tag
from resources.models import Document, Video, Article

def categories(request):
    latest_post = []
    latest_article = Article.objects.order_by('-created_at')[:2]
    latest_video = Video.objects.order_by('-created_at')[:2]
    latest_document = Document.objects.order_by('-created_at')[:2]
    latest_post.append(latest_article)
    latest_post.append(latest_video)
    latest_post.append(latest_document)  

        
    return {
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
        'latest_post': latest_post
    }