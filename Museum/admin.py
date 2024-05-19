from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.models import User

from datetime import date

from Museum.forms import PoemForm, GalleryPieceForm, EssayForm
from Museum.models import Poem, GalleryPiece, Essay
from members.models import Profile


# Filters

# Function to determine the correct ordinal indicator for centuries in the CenturyFilter
def ordinal(n):
    # The string "tsnrhtdd" is a clever way to map the numbers 0-3 to their corresponding ordinal indicators.
    # The expression inside the square brackets calculates the index based on the last digit of the number `n`,
    # unless `n` ends in 11, 12, or 13 (in which case it evaluates to 0).
    # This results in 't' for 0 (which is used for numbers ending in 0 or numbers ending in 4-9 or 11-13),
    # 's' for 1, 'n' for 2, and 'r' for 3.
    suffix = "tsnrhtdd"[((n // 10 % 10 != 1) * (n % 10 < 4) * n % 10)::4]

    # Return the number `n` followed by its corresponding ordinal indicator.
    return "%d%s" % (n, suffix)


# Filter a model's queryset based on the century an object was published, from the 1st century
# to the current century
class CenturyFilter(admin.SimpleListFilter):
    title = 'century published'
    parameter_name = 'century'

    def lookups(self, request, model_admin):
        current_year = date.today().year

        # Create a list of tuples with the century and its string representation
        # E.g. [(1, '1st century'), (2, '2nd century'), ...]
        return [(str(i), ('%s century' % ordinal(i))) for i in range(1, current_year // 100 + 2)]

    def queryset(self, request, queryset):
        if self.value():
            century = int(self.value())  # century specified by the user in the filter
            return queryset.filter(date_published__year__gte=(century - 1) * 100,
                                   date_published__year__lt=century * 100)


@admin.register(Poem)
class PoemAdmin(admin.ModelAdmin):
    form = PoemForm

    list_display = ('title', 'author', 'category', 'language', 'user', 'date_published', 'updated_at')
    search_fields = ['title', 'author', 'category', 'language', 'user__username', 'date_published', 'updated_at']
    list_filter = [CenturyFilter, 'language', 'category', 'author', 'user', 'date_published', 'updated_at']
    ordering = ['-updated_at']


@admin.register(GalleryPiece)
class GalleryPieceAdmin(admin.ModelAdmin):
    form = GalleryPieceForm

    list_display = (
        'title', 'piece_tag', 'piece', 'author', 'description', 'category', 'user', 'date_published', 'updated_at')
    search_fields = ['title', 'author', 'description', 'category', 'user__username', 'date_published', 'updated_at']
    list_filter = [CenturyFilter, 'author', 'category', 'user', 'date_published', 'updated_at']
    ordering = ['-updated_at']


@admin.register(Essay)
class EssayAdmin(admin.ModelAdmin):
    form = EssayForm

    list_display = (
        'title', 'author', 'file', 'is_academic', 'abstract', 'category', 'language', 'date_published', 'updated_at',
        'user')
    search_fields = ['title', 'author', 'file', 'is_academic', 'abstract', 'category', 'language', 'date_published',
                     'updated_at', 'user__username']
    list_filter = [CenturyFilter, 'author', 'is_academic', 'category', 'language', 'user', 'date_published',
                   'updated_at']
    ordering = ['-updated_at']


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    can_add = False
    extra = 0  # I set this on every inline so that the interface does not provide empty records
    fields = ['image_tag', 'bio', 'avatar', 'location', 'birth_date']
    readonly_fields = ['image_tag']


class PoemInline(admin.TabularInline):
    model = Poem
    extra = 0


class EssayInline(admin.TabularInline):
    model = Essay
    extra = 0
    fields = ['file', 'abstract', 'is_academic', 'category', 'language', 'date_published', 'updated_at']
    readonly_fields = ['pdf_cover', 'updated_at']


class GalleryPieceInline(admin.TabularInline):
    model = GalleryPiece
    extra = 0
    fields = ['piece_tag', 'piece', 'author', 'description', 'category', 'date_published', 'updated_at']
    readonly_fields = ['piece_tag', 'updated_at']


class UserAdmin(DefaultUserAdmin):
    inlines = [ProfileInline, PoemInline, EssayInline, GalleryPieceInline]
    extra = 0


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
