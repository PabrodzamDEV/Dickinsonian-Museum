from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from datetime import datetime

from .models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileForm(ModelForm):
    avatar = forms.ImageField(label='Profile Picture', required=False, widget=forms.FileInput(
        attrs={"id": "image_field"}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'location', 'birth_date']
        widgets = {
            "birth_date": forms.SelectDateWidget(years=range(datetime.now().year + 1, datetime.now().year - 110, -1)),
        }


class ProfileAdminForm(ModelForm):
    avatar = forms.ImageField(widget=forms.ClearableFileInput())

    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'location', 'birth_date']
