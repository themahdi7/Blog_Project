# Generated by Django 4.0.5 on 2022-07-30 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0014_alter_aboutus_biography'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', models.CharField(max_length=25, verbose_name='شماره تلفن')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('address', models.TextField(verbose_name='آدرس')),
                ('map_address', models.URLField(help_text='لینک ادرس خود را وارد کنید', verbose_name='لینک آدرس گوگل مپ')),
            ],
            options={
                'verbose_name': 'اطلاعات تماس',
                'verbose_name_plural': 'اطلاعات تماس',
            },
        ),
    ]