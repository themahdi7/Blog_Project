from django.contrib import admin
from .models import Message, AboutUs, ContactInfo, Footer



@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["name", "sub", "user"]


@admin.register(ContactInfo)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["phonenumber", "email"]


@admin.register(Footer)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["name", "link"]



admin.site.register(AboutUs)
