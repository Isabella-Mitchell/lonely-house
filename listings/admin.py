from django.contrib import admin
from .models import Listing, Category, Image, Facilities


class ImageInline(admin.TabularInline):
    model = Image


class FacilitiesInline(admin.TabularInline):
    model = Facilities


class ListingAdmin(admin.ModelAdmin):

    inlines = (ImageInline, FacilitiesInline, )

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
