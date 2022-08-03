from django.db import models
from django.contrib.auth.models import User


class AboutUs(models.Model):
    image = models.ImageField(upload_to="image/about_us_image", blank=True, null=True, verbose_name='تصویر اول صفحه')
    biography = models.TextField(blank=False, null=False, verbose_name='توضیحات  اصلی')
    first_subject = models.CharField(max_length=255, blank=True, null=True, verbose_name='موضوع ردیف اول')
    column = models.TextField(blank=True, null=True, verbose_name=" توضیحات ردیف اول")
    second_subject = models.CharField(max_length=255, blank=True, null=True, verbose_name='موضوع ردیف دوم')
    column2 = models.TextField(blank=True, null=True, verbose_name=" توضیحات ردیف دوم")
    instagram = models.URLField(blank=True, null=True, verbose_name="لینک اینستاگرام")
    twitter = models.URLField(blank=True, null=True, verbose_name="لینک توییتر")
    facebook = models.URLField(blank=True, null=True, verbose_name="لینک فیسبوک")
    linkedin = models.URLField(blank=True, null=True, verbose_name="لینک لینکدین")



    def __str__(self):
        return 'درباره ما'


    class Meta:
        verbose_name = ('درباره ما')
        verbose_name_plural = ('درباره ما')



class ContactInfo(models.Model):
    phonenumber = models.CharField(max_length=25, verbose_name="شماره تلفن")
    email = models.EmailField(verbose_name="ایمیل")
    address = models.TextField(verbose_name="آدرس")

    def __str__(self):
        return 'Contact Info'


    class Meta:
        verbose_name = ('اطلاعات تماس')
        verbose_name_plural = ('اطلاعات تماس')


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, verbose_name='کاربر')
    email = models.EmailField(verbose_name='ایمیل')
    name = models.CharField(max_length=30, verbose_name='نام')
    subject = models.CharField(max_length=150, verbose_name='موضوع')
    body = models.TextField(verbose_name='متن پیام')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"پیام از طرف '{self.user}'  "


    def sub(self):
        return f"{self.subject[:10]}..."
    sub.short_description = 'موضوع'


    class Meta:
        verbose_name = ('پیام')
        verbose_name_plural = ('پیام ها')


class Footer(models.Model):
    name = models.CharField(max_length=80, verbose_name='نام')
    link = models.URLField(verbose_name="لینک")

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = ('اطلاعات فوتر')
        verbose_name_plural = ('اطلاعات فوتر')