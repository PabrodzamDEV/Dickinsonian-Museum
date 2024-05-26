import os

from django import forms
from django.core.exceptions import ValidationError

from django_ckeditor_5.widgets import CKEditor5Widget

from datetime import datetime

from .models import Poem, GalleryPiece, Essay


class PoemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].required = True
        self.fields["content"].required = False  # Necessary for the CKEditor5 widget to work when validating the form
        self.fields["author"].required = True
        self.fields["category"].required = True
        self.fields["language"].required = True
        self.fields["user"].required = False
        self.fields["date_published"].required = False

    class Meta:
        model = Poem
        fields = ["title", "content", "author", "category", "language", "date_published", "user"]
        widgets = {
            "content": CKEditor5Widget(attrs={"class": "django_ckeditor_5"}),
            "date_published": forms.SelectDateWidget(years=range(0, datetime.now().year + 1)),
        }

    # Checks that the content field is not empty, otherwise raises a ValidationError
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise ValidationError('Please, do not leave the content field empty.')
        return content


class PoemFilterForm(forms.Form):
    # Let the user pick a category from the list of categories in the poem model
    category = forms.ModelChoiceField(queryset=Poem.objects.values_list('category', flat=True).distinct())


class GalleryPieceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].required = True
        self.fields["piece"].required = True
        self.fields["author"].required = True
        self.fields["description"].required = False  # Necessary for the CKEditor5 widget to work when validating the
        # form
        self.fields["category"].required = True
        self.fields["date_published"].required = False
        self.fields["user"].required = False

    class Meta:
        model = GalleryPiece
        fields = ["title", "piece", "author", "description", "category", "date_published", "user"]
        widgets = {
            "description": CKEditor5Widget(attrs={"class": "django_ckeditor_5"}),
            "date_published": forms.SelectDateWidget(years=range(0, datetime.now().year + 1)),
        }

    # Checks that the description field is not empty, otherwise raises a ValidationError
    def clean_content(self):
        description = self.cleaned_data.get('description')
        if not description:
            raise ValidationError('Please, do not leave the description field empty.')
        return description

    # Checks that the piece field does not exceed a given size, otherwise raises a ValidationError
    def clean_piece(self):
        piece = self.cleaned_data.get('piece')

        if piece:
            # Check the file size
            if piece.size > 100 * 1024 * 1024:  # maximum size allowed for the file
                raise forms.ValidationError("The maximum file size that can be uploaded is 100MB")

            # Check the file extension for allowed file types, otherwise raise a ValidationError
            ext = os.path.splitext(piece.name)[1]  # get the file extension
            valid_extensions = ['.jpeg', '.jpg', '.png', '.gif', '.webm', '.mp4']
            if not ext.lower() in valid_extensions:
                raise forms.ValidationError('Unsupported file extension.')

        return piece


class EssayForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].required = True
        self.fields["author"].required = True
        self.fields["file"].required = True
        self.fields["abstract"].required = False  # Necessary for the CKEditor5 widget to work when validating the
        # form
        self.fields["is_academic"].required = False
        self.fields["category"].required = True
        self.fields["language"].required = True
        self.fields["date_published"].required = False
        self.fields["user"].required = False

    class Meta:
        model = Essay
        fields = ["title", "author", "file", "is_academic", "abstract", "category", "language", "date_published",
                  "user"]
        widgets = {
            "abstract": CKEditor5Widget(attrs={"class": "django_ckeditor_5"}),
            "date_published": forms.SelectDateWidget(years=range(0, datetime.now().year + 1)),
        }

    # Only allow .pdf files as essays
    def clean_file(self):
        file = self.cleaned_data.get('file')

        if file:
            if not file.name.endswith('.pdf'):
                raise forms.ValidationError("Only PDF files are allowed.")
            return file
