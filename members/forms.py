from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
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
    class Meta:
        model = Profile
        fields = ['bio', 'avatar', 'location', 'birth_date']
