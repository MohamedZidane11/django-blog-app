from django.shortcuts import render
from .models import Article

# Create your views here.
def home(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'articles': articles})


def article_detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'blog/article_detail.html', {'article': article})
