from django.urls import path, re_path
from . import views

app_name = 'blog'
urlpatterns = [
    re_path(r'detail/(?P<slug>[-\w]+)/', views.article_detail, name='article_detail'),
    re_path(r'category/(?P<slug>[-\w]+)', views.category_detail, name='category_detail'),
    path('list', views.articles_list, name="articles_list"),
    path('search', views.search, name='search_article'),
]
