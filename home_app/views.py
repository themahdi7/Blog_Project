from django.shortcuts import render
from blog_app.models import Article



def home(request):
    articles = Article.objects.all()
    return render(request, "home_app/index.html", {'articles': articles})
