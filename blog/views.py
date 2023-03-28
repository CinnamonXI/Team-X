from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from django.contrib import messages 

# Create your views here.
def index(request):

    context = {
        'title': 'Blogs',
        'blogs': Post.objects.filter(is_published=True),
    }
    return render(request, 'blog.html', context)

def detail(request, slug):
    blog = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        comment = Comment(name=name, email=email, message=message, subject=subject, post=blog)
        comment.save()
        messages.success(request, 'Your comment has been submitted successfully!')
        return redirect('blogs:detail', slug=blog.slug)
    
    context = {
        'title': blog.title,
        'category': 'Blogs',
        'blog' : blog,
    }
    return render(request, 'blog-details.html', context)

def search(request): 
    try:
        if request.method == 'GET':
            search = request.GET.get('q')
            blogs = Post.objects.filter(title__icontains=search) or Post.objects.filter(body__icontains=search)
            context = {
                'title': f"Search result for '{search}'",
                'blogs': blogs,
            }
            return render(request, 'blog.html', context)
    except ValueError:
        return redirect('blogs:index')
    