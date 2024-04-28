from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from Museum.models import Poem

from .forms import PoemForm


# Create your views here.
def home(request):
    return render(request, "Museum/home.html")


"""
    Class-based view which renders a creation form for a poem.

    extends:
        django.views.generic.CreateView

"""


class PoemCreateView(CreateView):
    model = Poem
    form_class = PoemForm
    template_name = 'Museum/poem_form.html'  # Update this to your actual template
    success_url = reverse_lazy('poems')  # Update 'poems' to the name of your poems list view


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
