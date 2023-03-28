from django.shortcuts import render

# Create your views here.
def index(request):

    context = {
        'title': 'Blogs'
    }
    return render(request, 'blog.html', context)