from django.shortcuts import render, redirect
from blog_app.models import Article


def home(request):

    articles = Article.objects.filter(Release_Status=True)
    return render(request, "home_app/index.html", {'articles': articles})



def sidebar(request):
    context = {'name': 'sidebar'}
    return render(request, 'includes/sidebar.html', context)
