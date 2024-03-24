from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "Museum/home.html")


def poems(request):
    return render(request, "Museum/poems.html")


def gallery(request):
    return render(request, "Museum/gallery.html")


def essays(request):
    return render(request, "Museum/essays.html")


def contact(request):
    return render(request, "Museum/contact.html")
