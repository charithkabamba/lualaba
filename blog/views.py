from django.shortcuts import render

from .models import Blog, Category
# Create your views here.

def news(request):
    return render(request, 'blog/news.html')

def article(request):
    return render(request, 'blog/article.html')

def blog(request):
    blogs = Blog.objects.all()
    categories = Category.objects.all()
    context = {
        'blogs': blogs,
        'categories': categories,
    }
    return render(request, 'blog/blog.html', context)
