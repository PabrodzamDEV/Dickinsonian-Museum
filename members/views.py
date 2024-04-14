from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile

from members.forms import ProfileForm, SignUpForm


# Create your views here.
def login_member(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "There was an error logging in. Please try again")
            return redirect("login")
    else:
        form = AuthenticationForm()
    return render(request, "members/login.html", {"form": form})


@login_required()
def logout_member(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("login")


def register_member(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "members/register.html", {"form": form})


@login_required()
def update_profile(request):
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

    return render(request, "members/update_profile.html", {"form": form})
