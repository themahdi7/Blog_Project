from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class ArticleManager(models.Manager):
    def counter(self):
        return len(self.all())

    def published(self):
        return len(self.filter(Release_Status=True))


class Article(models.Model):

    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Category = models.ManyToManyField(Category)
    Title = models.CharField(max_length=70)
    Body = models.TextField()
    Image = models.ImageField(upload_to="image/article")
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now_add=True)
    Release_Status = models.BooleanField(default=False)
    objects = ArticleManager()


    def __str__(self):
        return f"{self.Title} - {self.Body[:30]}..."




