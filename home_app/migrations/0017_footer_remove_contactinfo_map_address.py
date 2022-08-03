# Generated by Django 4.0.5 on 2022-07-30 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0016_alter_contactinfo_map_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='نام')),
                ('link', models.URLField(verbose_name='لینک')),
            ],
            options={
                'verbose_name': 'اطلاعات فوتر',
                'verbose_name_plural': 'اطلاعات فوتر',
            },
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='map_address',
        ),
    ]