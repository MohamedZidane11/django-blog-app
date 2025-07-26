from django.shortcuts import render
from django.db.models import Q
from .models import Article

# Create your views here.
def home(request):
    search_query = request.GET.get('search')
    if search_query:
        articles = Article.objects.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query)
        ).order_by('-created_at')
    else:
        articles = Article.objects.all().order_by('-created_at')
    context = {
        'articles': articles,
        'search_query': search_query
    }
    return render(request, 'blog/home.html', context)


def article_detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'blog/article_detail.html', {'article': article})
