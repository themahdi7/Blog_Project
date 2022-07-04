from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


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
    Category = models.ManyToManyField(Category, related_name="articles")
    Title = models.CharField(max_length=70, unique=True)
    Body = models.TextField()
    Image = models.ImageField(upload_to="image/article")
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    Release_Status = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, unique=True, editable=False)  # for auto management links
    objects = ArticleManager()



    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.Title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('blog:article_detail',
                       kwargs={'slug': self.slug})  # ==  url templates tags {% url "blog:article_detail" article.id %}

    def __str__(self):
        return f"{self.Title} - {self.Body[:30]}..."
