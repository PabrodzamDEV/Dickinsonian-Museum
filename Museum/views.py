from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Museum.models import Poem


# Create your views here.
def home(request):
    return render(request, "Museum/home.html")


def poems(request):
    poem_list = Poem.objects.all()
    return render(request, "Museum/poems.html", {"poems": poem_list})


def gallery(request):
    return render(request, "Museum/gallery.html")


def essays(request):
    return render(request, "Museum/essays.html")


@login_required()
def contact(request):
    return render(request, "Museum/contact.html")
