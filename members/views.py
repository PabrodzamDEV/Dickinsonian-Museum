from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from members.forms import ProfileForm


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
        prof_form = ProfileForm
        return render(request, "members/login.html", {"prof_form": prof_form})


def logout_member(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("login")
