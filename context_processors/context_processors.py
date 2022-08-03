from blog_app.models import Article, Category
from home_app.models import Footer


def recent(request):
    footer = Footer.objects.all()
    recent = Article.objects.filter(Release_Status=True).order_by('-Created')[:3]
    return {'recent': recent, 'footer': footer}


def categories(request):
    categories = Category.objects.all()
    return {'categories': categories}
