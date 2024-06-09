import os

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from django import forms
from django.core.exceptions import ValidationError
from django.forms import SelectDateWidget

from django_ckeditor_5.widgets import CKEditor5Widget

from datetime import datetime

from .models import Poem, GalleryPiece, Essay


class HorizontalSelectDateWidget(SelectDateWidget):
    def build_attrs(self, base_attrs, extra_attrs=None):
        attrs = super().build_attrs(base_attrs, extra_attrs)
        attrs['class'] = 'd-flex flex-row'
        return attrs


class PoemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].required = True
        self.fields["title"].label = "Title"
        self.fields["content"].required = False  # Necessary for the CKEditor5 widget to work when validating the form
        self.fields["content"].label = "Poem's content"
        self.fields["author"].required = True
        self.fields["author"].label = "Author"
        self.fields["category"].required = True
        self.fields["category"].label = "Category"
        self.fields["language"].required = True
        self.fields["language"].label = "Language"
        self.fields["date_published"].required = False
        self.fields["date_published"].label = "Publication Date"

    class Meta:
        model = Poem
        fields = ["title", "content", "author", "category", "language", "date_published", "user"]
        widgets = {
            "content": CKEditor5Widget(attrs={"class": "django_ckeditor_5"}),
            "date_published": forms.SelectDateWidget(years=range(datetime.now().year + 1, 0, -1)),
        }

    # Checks that the content field is not empty, otherwise raises a ValidationError
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise ValidationError('Please, do not leave the content field empty.')
        return content


class PoemCreateForm(PoemForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Create poem', css_class='btn-primary'))
    helper.form_method = 'POST'

    class Meta(PoemForm.Meta):
        exclude = ["user"]


class PoemUpdateForm(PoemCreateForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Update poem', css_class='btn-primary'))


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

    class Meta:
        model = GalleryPiece
        fields = ["title", "piece", "author", "description", "category", "date_published", "user"]
        widgets = {
            "description": CKEditor5Widget(attrs={"class": "django_ckeditor_5"}),
            "date_published": forms.SelectDateWidget(
                years=range(datetime.now().year + 1, 0, -1)),
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


class GalleryPieceCreateForm(GalleryPieceForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Create piece', css_class='btn-primary'))
    helper.form_method = 'POST'

    class Meta(GalleryPieceForm.Meta):
        exclude = ["user"]


class GalleryPieceUpdateForm(GalleryPieceCreateForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Update piece', css_class='btn-primary'))


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


class EssayCreateForm(EssayForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Create essay', css_class='btn-primary'))
    helper.form_method = 'POST'

    class Meta(EssayForm.Meta):
        exclude = ["user"]


class EssayUpdateForm(EssayCreateForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Update essay', css_class='btn-primary'))
