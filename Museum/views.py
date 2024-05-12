from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from Museum.models import Poem

from .forms import PoemForm


# Create your views here.
def home(request):
    return render(request, "Museum/home.html")


"""
    Class-based view which renders a creation form for a poem.

    extends:
        django.views.generic.edit.CreateView

"""


class PoemCreateView(LoginRequiredMixin, CreateView):
    model = Poem
    form_class = PoemForm
    template_name = 'Museum/poem_form.html'
    success_url = reverse_lazy('poems')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


"""
    Class-based view which renders the whole collection of poems present in the database, ordered
    by title.

    extends:
        django.views.generic.list.ListView

"""


class PoemListView(ListView):
    model = Poem
    template_name = 'Museum/poems.html'
    context_object_name = 'poems'
    ordering = ['title']


"""
    Class-based view which renders a form to update a specific poem.

    extends:
        django.views.generic.edit.UpdateView

"""


class PoemUpdateView(LoginRequiredMixin, UpdateView):
    model = Poem
    fields = ['title', 'content', 'author', 'category', 'language', 'date_published']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('poems')


"""
    Class-based view which allows the deletion of a specific poem.

    extends:
        django.views.generic.edit.DeleteView

"""


class PoemDeleteView(LoginRequiredMixin, DeleteView):
    model = Poem
    template_name = 'Museum/poem_confirm_delete.html'
    success_url = reverse_lazy('poems')


def gallery(request):
    return render(request, "Museum/gallery.html")


def essays(request):
    return render(request, "Museum/essays.html")


@login_required()
def contact(request):
    return render(request, "Museum/contact.html")
