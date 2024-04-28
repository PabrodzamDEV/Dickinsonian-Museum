from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from Museum.models import Poem


# Create your views here.
def home(request):
    return render(request, "Museum/home.html")


"""
    Class-based view which renders the whole collection of poems present in the database, ordered
    by title.

    extends:
        django.views.generic.ListView

"""


class PoemListView(ListView):
    model = Poem
    template_name = 'Museum/poems.html'
    context_object_name = 'poems'
    ordering = ['title']


def gallery(request):
    return render(request, "Museum/gallery.html")


def essays(request):
    return render(request, "Museum/essays.html")


@login_required()
def contact(request):
    return render(request, "Museum/contact.html")
