from django.shortcuts import render, get_object_or_404
from .models import Article, Category


def article_detail(request, slug):  # pk = primary key
    article = get_object_or_404(Article.objects.filter(Release_Status=True), slug=slug)
    return render(request, "blog_app/article_details.html", {'article': article})


def articles_list(request):
    articles = Article.objects.filter(Release_Status=True)
    return render(request, "blog_app/articles_list.html", {'articles': articles})



def category_detail(request, pk=None):  # pk = primary key
    category = get_object_or_404(Category, id=pk)
    articles = category.articles.all()
    return render(request, "blog_app/articles_list.html", {'articles': articles})

