from django.contrib import admin
from .forms import ProfileAdminForm
from .models import Profile


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm
    list_display = ('user', 'bio', 'image_tag', 'avatar', 'location', 'birth_date')
    fields = ['image_tag', 'user', 'bio', 'avatar', 'location', 'birth_date']
    ordering = ['user']
    readonly_fields = ['image_tag']


admin.site.register(Profile, ProfileAdmin)