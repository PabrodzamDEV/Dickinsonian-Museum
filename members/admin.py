from django.contrib import admin
from .forms import ProfileAdminForm
from .models import Profile


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm


admin.site.register(Profile, ProfileAdmin)