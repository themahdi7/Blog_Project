# Generated by Django 4.0.5 on 2022-07-31 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0040_remove_article_like_alter_article_slug_delete_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, unique=True),
        ),
    ]
