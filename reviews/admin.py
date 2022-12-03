from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        'listing',
        'user_profile',
        'rating',
        'review_title',
        'featured',
    )


admin.site.register(Review, ReviewAdmin)
