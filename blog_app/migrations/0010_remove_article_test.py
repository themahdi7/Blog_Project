# Generated by Django 4.0.5 on 2022-06-29 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_article_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='Test',
        ),
    ]
