# Generated by Django 4.0.5 on 2022-07-12 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_profile_fathers_name_remove_profile_melicode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile'),
        ),
    ]