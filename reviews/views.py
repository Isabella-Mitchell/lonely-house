from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from profiles.models import UserProfile

from .models import Review
from .forms import ReviewForm


def reviews(request):

    template = 'reviews/reviews.html'

    return render(request, template)


def add_review(request):
    """A view to return the reviews page"""

    # profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.user)
     
        if form.is_valid():
            print(form)
            form.save()
            messages.success(request, 'Review saved successfully')
            return redirect(reverse('add_review'))
        else:
            messages.error(request, 'Failed, please try again')
    else:
        form = ReviewForm()

    # reviews = Review.objects.all()
    # user_reviews = reviews.filter(user_profile=profile)

    template = 'reviews/add_review.html'
    context = {
        'form': form,
        # 'profile': profile,
        # 'user_reviews': user_reviews,
    }

    return render(request, template, context)


def edit_review(request, review_id):

    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated review!')
            return redirect(reviews)
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing a review')

    template = 'reviews/edit_review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)
