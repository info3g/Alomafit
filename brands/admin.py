from django.contrib import admin

from brands.models import Brand, Size, ProductType

admin.site.register(Size)
admin.site.register(Brand)
admin.site.register(ProductType)
