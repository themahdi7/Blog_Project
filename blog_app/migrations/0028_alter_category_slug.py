# Generated by Django 4.0.5 on 2022-07-05 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0027_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]