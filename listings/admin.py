from django.contrib import admin
from .models import Listing, Category

# Register your models here.
admin.site.register(Listing)
admin.site.register(Category)
