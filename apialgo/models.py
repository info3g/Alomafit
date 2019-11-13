from django.db import models


class Measurements(models.Model):
    bra_size = models.DecimalField(max_digits=20, decimal_places=2)
    brand_name = models.CharField(max_length=50)
    cap_pra_unit_value = models.CharField(max_length=50)
    cap_size = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    height = models.DecimalField(max_digits=20, decimal_places=2)
    height_unit = models.CharField(max_length=50)
    product_type = models.CharField(max_length=50)
    product_image_one = models.URLField(max_length=200)
    product_image_two = models.URLField(max_length=200)
    selected_fat = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=20, decimal_places=2)
    weight_unit = models.CharField(max_length=50)
