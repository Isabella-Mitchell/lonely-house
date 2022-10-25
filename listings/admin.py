from django.contrib import admin
from .models import Listing, Category


class ListingAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'country',
        'no_sleeps',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


admin.site.register(Listing, ListingAdmin)
admin.site.register(Category, CategoryAdmin)
