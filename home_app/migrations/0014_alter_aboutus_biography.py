# Generated by Django 4.0.5 on 2022-07-30 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0013_aboutus_facebook_aboutus_instagram_aboutus_linkedin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='biography',
            field=models.TextField(verbose_name='توضیحات  اصلی'),
        ),
    ]
