from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def login_member(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            msg = "You are logged in as '%s'" % username
            messages.success(request, msg)
            return redirect("home")
        else:
            messages.error(request, "There was an error logging in. Please try again")
            return render(request, "members/login.html")
    else:
        return render(request, "members/login.html")


def logout_member(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("login")
