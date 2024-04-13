from django.contrib import admin
from.forms import ProfileForm
from .models import Profile


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileForm


admin.site.register(Profile, ProfileAdmin)