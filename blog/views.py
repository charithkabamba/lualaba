from django.shortcuts import render

# Create your views here.

def news(request):
    return render(request, 'blog/news.html')

def article(request):
    return render(request, 'blog/article.html')

def blog(request):
    return render(request, 'blog/blog.html')
