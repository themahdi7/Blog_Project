from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout



def userlogin(request):

    if request.user.is_authenticated == True:
        return redirect('home_app:home')
    if request.method == "POST":  # check form method
        username = request.POST.get('username')  # get the username from user
        password = request.POST.get('password')  # get the password from user
        user = authenticate(request, username=username, password=password)  # check the username and password entered by the user
        if user is not None:
            # if username and password is true do this:
            login(request, user)
            return redirect('home_app:home')
            # back to home page

    return render(request, "account/login.html", {})


def user_register(request):
    context = {"errors": []}
    if request.user.is_authenticated == True:
        return redirect('home_app:home')

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            context['errors'].append('Passwords does not match')
            return render(request, "account/register.html", context)

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        return redirect('home_app:home')


    return render(request, "account/register.html", {})

def user_logout(request):
    logout(request)
    return redirect('home_app:home')
