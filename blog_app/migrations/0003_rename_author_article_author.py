# Generated by Django 4.0.5 on 2022-06-27 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_article_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author',
            new_name='Author',
        ),
    ]
