from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from Museum.models import Poem, GalleryPiece, Essay

from .forms import PoemForm, GalleryPieceForm


# Create your views here.
def home(request):
    return render(request, "Museum/home.html")


"""
    Class-based view which renders the whole collection of poems present in the database, ordered
    by title.

    extends:
        django.contrib.auth.mixins.LoginRequiredMixin
        django.views.generic.list.ListView

"""


class PoemListView(ListView):
    model = Poem
    template_name = 'Museum/poems.html'
    context_object_name = 'poems'
    ordering = ['title']


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
        django.contrib.auth.mixins.LoginRequiredMixin
        django.views.generic.edit.DeleteView

"""


class PoemDeleteView(LoginRequiredMixin, DeleteView):
    model = Poem
    template_name = 'Museum/poem_confirm_delete.html'
    success_url = reverse_lazy('poems')


"""
    Class-based view which renders the whole collection of gallery pieces present in the database, ordered
    by title.

    extends:
        django.contrib.auth.mixins.LoginRequiredMixin
        django.views.generic.list.ListView

"""


class GalleryPieceListView(ListView):
    model = GalleryPiece
    template_name = 'Museum/gallery.html'
    context_object_name = 'gallery_pieces'
    ordering = ['title']


"""
    Class-based view which renders a creation form for a gallery piece.

    extends:
        django.contrib.auth.mixins.LoginRequiredMixin
        django.views.generic.edit.CreateView

"""


class GalleryPieceCreateView(LoginRequiredMixin, CreateView):
    model = GalleryPiece
    form_class = GalleryPieceForm
    template_name = 'Museum/gallery_piece_form.html'
    success_url = reverse_lazy('gallery')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


"""
    Class-based view which renders a form to update a specific gallery piece.

    extends:
        django.contrib.auth.mixins.LoginRequiredMixin
        django.views.generic.edit.UpdateView

"""


class GalleryPieceUpdateView(LoginRequiredMixin, UpdateView):
    model = GalleryPiece
    fields = ['title', 'piece', 'author', 'description', 'category', 'date_published']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('gallery')


"""
    Class-based view which allows the deletion of a specific gallery piece.

    extends:
        django.contrib.auth.mixins.LoginRequiredMixin
        django.views.generic.edit.DeleteView

"""


class GalleryPieceDeleteView(LoginRequiredMixin, DeleteView):
    model = GalleryPiece
    template_name = 'Museum/gallery_piece_confirm_delete.html'
    success_url = reverse_lazy('gallery')


# """
#     Class-based view which renders the whole collection of essays present in the database, ordered
#     by title.
#
#     extends:
#         django.contrib.auth.mixins.LoginRequiredMixin
#         django.views.generic.list.ListView
#
# """
#
#
# class EssayListView(ListView):
#     model = Essay
#     template_name = 'Museum/essays.html'
#     context_object_name = 'essays'
#     ordering = ['title']
#
#
# """
#     Class-based view which renders a creation form for an essay.
#
#     extends:
#         django.views.generic.edit.CreateView
#
# """
#
#
# class EssayCreateView(LoginRequiredMixin, CreateView):
#     model = Essay
#     form_class = EssayForm
#     template_name = 'Museum/essay_form.html'
#     success_url = reverse_lazy('essays')
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
#
#
# """
#     Class-based view which renders a form to update a specific essay.
#
#     extends:
#         django.views.generic.edit.UpdateView
#
# """
#
#
# class EssayUpdateView(LoginRequiredMixin, UpdateView):
#     model = Essay
#     fields = ['title', 'content', 'author', 'category', 'language', 'date_published']
#     template_name_suffix = '_update_form'
#     success_url = reverse_lazy('essays')
#
#
# """
#     Class-based view which allows the deletion of a specific essay.
#
#     extends:
#         django.contrib.auth.mixins.LoginRequiredMixin
#         django.views.generic.edit.DeleteView
#
# """
#
#
# class EssayDeleteView(LoginRequiredMixin, DeleteView):
#     model = Essay
#     template_name = 'Museum/essay_confirm_delete.html'
#     success_url = reverse_lazy('essays')


@login_required()
def contact(request):
    return render(request, "Museum/contact.html")
