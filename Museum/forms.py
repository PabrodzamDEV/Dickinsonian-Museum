from django import forms
from django.core.exceptions import ValidationError

from django_ckeditor_5.widgets import CKEditor5Widget

from .models import Poem


class PoemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].required = True
        self.fields["content"].required = False  # Necessary for the CKEditor5 widget to work when validating the form
        self.fields["author"].required = True
        self.fields["category"].required = True
        self.fields["language"].required = True
        self.fields["uploaded_by"].required = False
        self.fields["date_published"].required = False

    class Meta:
        model = Poem
        fields = ["title", "content", "author", "category", "language", "date_published", "uploaded_by"]
        widgets = {
            "content": CKEditor5Widget(attrs={"class": "django_ckeditor_5"}),
        }

    # Checks that the content field is not empty, otherwise raises a ValidationError
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise ValidationError('Please, do not leave the content field empty.')
        return content
