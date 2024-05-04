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
    template_name = 'Museum/poem_form.html'
    success_url = reverse_lazy('poems')

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)


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
