from django.contrib.postgres.fields import JSONField
from django.db import models

from stores.models import Store


class Brand(models.Model):
    name = models.CharField(max_length=50, default="", null=False, blank=False)
    gender = models.CharField(max_length=50, default="female", null=True)
    part = models.CharField(max_length=50, default="", null=True, blank=True)
    sizes = models.CharField(max_length=255, default="", null=True)
    measurements = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, null=True, blank=True)
    # product_types = JSONField()
    product_types = models.CharField(max_length=50, default="", null=True, blank=True)
    category = models.CharField(max_length=50, default="", null=True, blank=True)
    unit = models.CharField(max_length=50, default="", null=True, blank=True)
    store_slug = models.CharField(max_length=100, default="", null=True, blank=True)

    def __str__(self):
        return "Brand {0} For {1}".format(self.name, self.gender)


class Size(models.Model):
    title = models.CharField(max_length=50, default="", null=False, blank=False)
    bust = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, null=True, blank=True)
    hips = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, null=True, blank=True)
    waist = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, null=True, blank=True)

    def __str__(self):
        return "Size {0}".format(self.title)


class ProductType(models.Model):
    name = models.CharField(max_length=50, default="", null=False, blank=False)
    unit = models.CharField(max_length=50, default="", null=False, blank=False)
    sizes = models.ManyToManyField(to=Size)

    def __str__(self):
        return "ProductType {0}".format(self.name)
