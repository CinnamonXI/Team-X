from .models import Category, Tag

def categories(request):
    return {
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
    }