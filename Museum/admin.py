from django.contrib import admin
from Museum.forms import PoemForm, GalleryPieceForm, EssayForm
from Museum.models import Poem, GalleryPiece, Essay


@admin.register(Poem)
class PoemAdmin(admin.ModelAdmin):
    form = PoemForm

    list_display = ('title', 'author', 'category', 'language', 'user', 'date_published', 'updated_at')


@admin.register(GalleryPiece)
class GalleryPieceAdmin(admin.ModelAdmin):
    form = GalleryPieceForm

    list_display = ('title', 'piece', 'author', 'description', 'category', 'date_published', 'updated_at', 'user')


@admin.register(Essay)
class GalleryPieceAdmin(admin.ModelAdmin):
    form = EssayForm

    list_display = (
        'title', 'author', 'file', 'is_academic', 'abstract', 'category', 'language', 'date_published', 'updated_at',
        'user')
