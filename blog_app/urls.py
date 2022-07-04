from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('detail/<slug:slug>', views.article_detail, name='article_detail'),
    path('list', views.articles_list, name="articles_list"),
    path('category/<int:pk>', views.category_detail, name='category_detail'),

]
