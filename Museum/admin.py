from django.contrib import admin
from Museum.forms import PoemForm
from Museum.models import Poem
from django.utils import timezone


# Register your models here.
class PoemAdmin(admin.ModelAdmin):
    form = PoemForm

    def save_model(self, request, obj, form, change):
        obj.updated_at = timezone.now()  # Set updated_at to current date and time

        if not change and not obj.uploaded_by_id:
            obj.uploaded_by = request.user  # Assign the currently logged-in user

        super().save_model(request, obj, form, change)


admin.site.register(Poem, PoemAdmin)
