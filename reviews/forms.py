from django.shortcuts import get_object_or_404
from django import forms
from .models import Review
from profiles.models import UserProfile


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user_profile','featured',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
