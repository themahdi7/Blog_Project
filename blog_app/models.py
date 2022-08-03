from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='عنوان')
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, unique=True, editable=False, allow_unicode=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Category, self).save()

    def get_absolute_url(self):
        return reverse('blog:category_detail',
                       kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = ('دسته بندی')
        verbose_name_plural = ('دسته بندی ها')


class ArticleManager(models.Manager):
    def counter(self):
        return len(self.all())

    def published(self):
        return len(self.filter(Release_Status=True))


class Article(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
    Category = models.ManyToManyField(Category, related_name="articles", verbose_name='دسته بندی')
    Title = models.CharField(max_length=70, unique=True, verbose_name='عنوان')
    Body = models.TextField(verbose_name='متن مقاله')
    Image = models.ImageField(upload_to="image/article", verbose_name='تصویر')
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    Release_Status = models.BooleanField(default=False, verbose_name='وضعیت انتشار')
    slug = models.SlugField(blank=True, unique=True, editable=False, allow_unicode=True)
    objects = ArticleManager()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        self.slug = slugify(self.Title, allow_unicode=True)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:article_detail',
                       kwargs={'slug': self.slug})

    class Meta:
        ordering = ('-Created',)
        verbose_name = ('مقاله')
        verbose_name_plural = ('مقالات')

    def __str__(self):
        return self.Title

    def body_object(self):
        return f"{self.Body[:15]}..."

    body_object.short_description = 'متن مقاله'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='مقاله')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='کاربر')
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name='replies',
                               verbose_name='کاربر والد')

    body = models.TextField(verbose_name='متن نظر')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"نظر کاربر'{self.user}'  "

    def comment(self):
        return f"{self.body[:15]}"

    comment.short_description = 'متن نظر'

    class Meta:
        verbose_name = ('نظر')
        verbose_name_plural = ('نظرات')
