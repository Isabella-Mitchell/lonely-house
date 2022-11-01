from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Listing(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    region = models.CharField(max_length=254, null=True, blank=True)
    country = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    no_sleeps = models.DecimalField(max_digits=6, decimal_places=0)
    description = models.TextField(null=True, blank=True)
    map_embed = models.TextField(null=True, blank=True)
    latitude = models.DecimalField(
        max_digits=12, decimal_places=10, null=True, blank=True)
    longitude = models.DecimalField(
        max_digits=12, decimal_places=10, null=True, blank=True)
    dog_friendly = models.BooleanField(default=False)
    wheelchair_accessible = models.BooleanField(default=False)
    hot_water = models.BooleanField(default=False)
    central_heating = models.BooleanField(default=False)
    fireplace = models.BooleanField(default=False)
    bath = models.BooleanField(default=False)
    shower = models.BooleanField(default=False)
    washing_machine = models.BooleanField(default=False)
    hob = models.BooleanField(default=False)
    oven = models.BooleanField(default=False)
    fridge = models.BooleanField(default=False)
    tv = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    bbq = models.BooleanField(default=False)
    cot = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Image(models.Model):
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=254, null=True, blank=True)
