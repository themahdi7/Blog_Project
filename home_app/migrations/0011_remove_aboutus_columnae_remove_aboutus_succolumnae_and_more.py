# Generated by Django 4.0.5 on 2022-07-30 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0010_alter_aboutus_options_aboutus_succolumnae'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='columnae',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='succolumnae',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='Second_subject',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='موضوع ردیف دوم'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='column',
            field=models.TextField(blank=True, null=True, verbose_name=' توضیحات ردیف اول'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='column2',
            field=models.TextField(blank=True, null=True, verbose_name=' توضیحات ردیف اول'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='first_subject',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='موضوع ردیف اول'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='biography',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات  اصلی'),
        ),
    ]
