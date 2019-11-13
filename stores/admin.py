from django.contrib import admin

from stores.models import *


class AdminStore(admin.ModelAdmin):
    readonly_fields = ['url', 'token', 'slug', 'owner', ]


class AdminProduct(admin.ModelAdmin):
    readonly_fields = ['shopify_id', 'title',
                       'image', 'updated_at', 'available_online',
                       'created_at', 'vendor']


class AdminVariant(admin.ModelAdmin):
    readonly_fields = ['shopify_id', 'product']


admin.site.register(Store, AdminStore)
admin.site.register(Product, AdminProduct)
admin.site.register(Variant, AdminVariant)
admin.site.register(RecurringCharge)
