from django.contrib import admin
from.forms import ProfileForm
from .models import Profile
from django.utils import timezone


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileForm

    # def save_model(self, request, obj, form, change):
    #     obj.updated_at = timezone.now()  # Set updated_at to current date and time
    #
    #     if not change and not obj.uploaded_by_id:
    #         obj.uploaded_by = request.user  # Assign the currently logged-in user
    #
    #     super().save_model(request, obj, form, change)


admin.site.register(Profile, ProfileAdmin)