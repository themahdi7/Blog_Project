from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def article_detail(request, slug):
    article = get_object_or_404(Article.objects.filter(Release_Status=True), slug=slug)
    if request.method == 'POST':
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(body=body, article=article, user=request.user, parent_id=parent_id)
    return render(request, "blog_app/article_details.html", {'article': article})


def articles_list(request):
    articles = Article.objects.filter(Release_Status=True)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 6)

    try:
        object_list = paginator.get_page(page_number)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)

    return render(request, "blog_app/articles_list.html", {'articles': object_list})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = category.articles.all()
    return render(request, "blog_app/articles_list.html", {'articles': articles})


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(Release_Status=True, Title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 6)

    try:
        object_list = paginator.get_page(page_number)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)
    return render(request, "blog_app/articles_list.html", {'articles': object_list})
