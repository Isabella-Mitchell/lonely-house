from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from profiles.models import UserProfile

from .models import Review
from .forms import ReviewForm


@login_required
def reviews(request):
    """A view to return the reviews page"""

    profile = get_object_or_404(UserProfile, user=request.user)

    reviews = Review.objects.all()
    user_reviews = reviews.filter(user_profile=profile)

    template = 'reviews/reviews.html'

    context = {
        'profile': profile,
        'user_reviews': user_reviews,
        'on_review_page': True,
    }

    return render(request, template, context)


@login_required
def add_review(request):
    """Users can add a review"""

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
     
        if form.is_valid():
            form.instance.user_profile = profile
            form.save()
            messages.success(request, 'Review saved successfully')
            return redirect(reverse('add_review'))
        else:
            messages.error(request, 'Failed, please try again')
    else:
        form = ReviewForm()

    template = 'reviews/add_review.html'
    context = {
        'form': form,
        # 'profile': profile,
        # 'user_reviews': user_reviews,
    }

    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """User can edit their reviews"""

    profile = get_object_or_404(UserProfile, user=request.user)

    review = get_object_or_404(Review, pk=review_id)
    # print(request.user)
    # print(review.user_profile.user)
    if request.user != review.user_profile.user:
        messages.error(request, "You do not have permission to edit this review")
        return redirect('home')

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.instance.user_profile = profile
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


@login_required
def delete_review(request, review_id):
    """User can delete their reviews"""
    review = get_object_or_404(Review, pk=review_id)
    if request.user != review.user_profile.user:
        messages.error(request, "You do not have permission to delete this review")
        return redirect('home')

    review.delete()
    messages.success(request, 'Review successfully deleted')
    return redirect(reviews)
