# Generated by Django 4.0.5 on 2022-07-30 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0009_aboutus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name': 'درباره ما', 'verbose_name_plural': 'درباره ما'},
        ),
        migrations.AddField(
            model_name='aboutus',
            name='succolumnae',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
