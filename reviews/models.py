from django.db import models

from listings.models import Listing
from profiles.models import UserProfile
from django.core.validators import MaxValueValidator, MinValueValidator
# from django.contrib.auth.models import User


class Review(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=False, blank=False)
    review_title = models.CharField(max_length=254, null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    featured = models.BooleanField(default=False)
