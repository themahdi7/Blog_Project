from django.contrib import admin
from .models import Article, Category, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["Title", "body_object", "Author", "Release_Status"]
    search_fields = ["Title"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ["name"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "comment", "article"]
