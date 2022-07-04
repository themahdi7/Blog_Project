from blog_app.models import Article, Category


def recent(request):

    recent = Article.objects.filter(Release_Status=True).order_by('-Created')[:3]
    return {'recent': recent}

def categories(request):
    categories = Category.objects.all()
    return {'categories': categories}
