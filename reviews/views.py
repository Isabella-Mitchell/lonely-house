from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from profiles.models import UserProfile

from .models import Review
from .forms import ReviewForm


def reviews(request):
    """A view to return the reviews page"""

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            messages.success(request, 'Review saved successfully')

    form = ReviewForm()

    reviews = Review.objects.all()
    user_reviews = reviews.filter(user_profile=profile)

    template = 'reviews/reviews.html'
    context = {
        'form': form,
        'profile': profile,
        'user_reviews': user_reviews,
    }

    return render(request, template, context)
