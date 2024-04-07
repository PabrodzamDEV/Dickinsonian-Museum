from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile

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


def create_profile(request):
    try:
        # Attempt to get the profile for the current user
        profile = request.user.profile
        # If profile exists, set instance attribute of the form to the existing profile
        form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    except Profile.DoesNotExist:
        # If profile doesn't exist, initialize form without instance
        form = ProfileForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            # Save the form
            form.save()
            return redirect("home")

    return render(request, "members/create_profile.html", {"form": form})
