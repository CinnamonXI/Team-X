from django.shortcuts import render

# Create your views here.
def article(request):
    context = {
        'title': 'Resource Articles',
    }
    return render(request, 'resources/index.html', context)

def video(request):
    context = {
        'title': 'Resource Videos',
    }
    return render(request, 'resources/videos.html', context)

def documents(request):
    context = {
        'title': 'Resource Documents',
    }
    return render(request, 'resources/documents.html', context)