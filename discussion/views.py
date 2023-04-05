from django.shortcuts import render

# Create your views here.
def ask(request):
    return render(request, 'forum/ask-questions.html')