from django.contrib import admin
from .models import Listing, Category, Image


class ImageInline(admin.TabularInline):
    model = Image


class ListingAdmin(admin.ModelAdmin):

    inlines = (ImageInline,)

    list_display = (
        'name',
        'category',
        'price',
        'country',
        'no_sleeps',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


admin.site.register(Listing, ListingAdmin)
admin.site.register(Category, CategoryAdmin)
