# Generated by Django 4.0.5 on 2022-07-30 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0008_alter_message_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/about_us_image', verbose_name='تصویر اول صفحه')),
                ('biography', models.TextField(blank=True, null=True, verbose_name='توضیحات ')),
                ('columnae', models.TextField(blank=True, null=True, verbose_name='ستون اول')),
            ],
        ),
    ]