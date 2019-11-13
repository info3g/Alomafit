from django.db import models

from stores.models import Store


class Theme(models.Model):
    store = models.OneToOneField(Store, on_delete=models.CASCADE, primary_key=True)
    try_it_text = models.CharField(max_length=200)
    modal_position = models.CharField(max_length=200)
    color_theme = models.CharField(max_length=200)
    logo_image = models.ImageField(upload_to='logos', max_length=255)

    def __str__(self):
        return "Theme for: " + self.store.url
