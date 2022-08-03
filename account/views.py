from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import LoginForm, RegisterForm, ProfileForm


def userlogin(request):
    if request.user.is_authenticated == True:
        return redirect('home_app:home')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('home_app:home')

    else:
        form = LoginForm()
    return render(request, "account/login.html", {'form': form})


def user_register(request):
    if request.user.is_authenticated == True:
        return redirect('home_app:home')

    form = RegisterForm(request.POST)
    if form.is_valid():
        user_email = form.cleaned_data.get('email')
        user_username = form.cleaned_data.get('username')
        user_password = form.cleaned_data.get('password')
        # check username and email
        user_name: bool = User.objects.filter(username=user_username).exists()
        user_email: bool = User.objects.filter(email__iexact=user_email).exists()
        if user_name:
            form.add_error('username', 'This username already exists')

        elif user_email:
            form.add_error('email', 'Looks like you already have a user. Did you try logging in?')

        else:
            new_user = User(email=user_email, username=user_username)
            new_user.set_password(user_password)
            new_user.save()
            login(request, new_user)
            return redirect('home_app:home')
    return render(request, "account/register.html", {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home_app:home')


def user_profile(request):
    if request.user.is_authenticated == False:
        return redirect('home_app:home')

    user = request.user
    form = ProfileForm(instance=user)

    if request.method == 'POST':
        form = ProfileForm(instance=user, data=request.POST)
        if form.is_valid():
            user_first_name = form.cleaned_data.get('first_name')
            user_last_name = form.cleaned_data.get('last_name')
            form.save()
    return render(request, 'account/edit_profile.html', {'form': form})
