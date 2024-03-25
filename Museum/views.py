from django.shortcuts import render

from Museum.models import Poem


# Create your views here.
def home(request):
    return render(request, "Museum/home.html")


def poems(request):
    poems = Poem.objects.all()
    return render(request, "Museum/poems.html", {"poems": poems})


def gallery(request):
    return render(request, "Museum/gallery.html")


def essays(request):
    return render(request, "Museum/essays.html")


def contact(request):
    return render(request, "Museum/contact.html")
