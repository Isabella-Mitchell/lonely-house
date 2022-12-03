from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    featured = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Facility(models.Model):
    class Meta:
        verbose_name_plural = 'Facilities'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    font_awesome_class = models.CharField(
        max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Listing(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)  # required
    region = models.CharField(max_length=254, null=True, blank=True)
    country = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)  # required
    no_sleeps = models.DecimalField(max_digits=6, decimal_places=0)  # required
    description = models.TextField(null=True, blank=True)
    latitude = models.DecimalField(
        max_digits=12, decimal_places=10, null=False, blank=False)
    longitude = models.DecimalField(
        max_digits=12, decimal_places=10, null=False, blank=False)
    featured = models.BooleanField(default=False)
    lead_image = models.ImageField(null=True, blank=True)
    lead_image_url = models.URLField(max_length=1024, null=True, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    capacity = models.DecimalField(
        max_digits=2, decimal_places=0, null=True, blank=True, default=1)

    def __str__(self):
        return self.name


class Image(models.Model):
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=254, null=True, blank=True)
