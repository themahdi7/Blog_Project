from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login



def userlogin(request):
    if request.method == "POST":  # check form method
        username = request.POST.get('username')  # get the username from user
        password = request.POST.get('password')  # get the password from user
        user = authenticate(request, username=username, password=password)  # check the username and password entered by the user
        if user is not None:  # if username and password is true do this:
            login(request, user)
            return redirect('/')   # back to home page

    return render(request, "account/login.html", {})
