from django.contrib import admin
from .models import Listing, Category, Image, Facility


class ImageInline(admin.TabularInline):
    model = Image


class ListingAdmin(admin.ModelAdmin):

    inlines = (ImageInline, )

    list_display = (
        'name',
        'category',
        'price',
        'country',
        'no_sleeps',
        'featured',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'featured',
    )


class FacilityAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'font_awesome_class'
    )


admin.site.register(Listing, ListingAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Facility, FacilityAdmin)
