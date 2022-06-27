from django.db import models
from django.contrib.auth.models import User



class Article(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=70)
    Body = models.TextField()
    Image = models.ImageField(upload_to="image/article")
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.Title} - {self.Body[:30]}..."
