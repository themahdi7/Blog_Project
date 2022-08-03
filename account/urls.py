from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path("login", views.userlogin, name="login"),
    path("logout", views.user_logout, name="logout"),
    path("register", views.user_register, name="register"),
    path("profile", views.user_profile, name="Profile"),

]
