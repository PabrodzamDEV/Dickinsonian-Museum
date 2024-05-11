from django.contrib import admin
from Museum.forms import PoemForm
from Museum.models import Poem
from django.utils import timezone


# Register your models here.
class PoemAdmin(admin.ModelAdmin):
    form = PoemForm

    list_display = ('title', 'author', 'category', 'language', 'user', 'date_published', 'updated_at')

    def save_model(self, request, obj, form, change):
        obj.updated_at = timezone.localtime()  # Set updated_at to current date and time

        if not change and not obj.user_id:
            obj.user = request.user  # Assign the currently logged-in user

        super().save_model(request, obj, form, change)


admin.site.register(Poem, PoemAdmin)
