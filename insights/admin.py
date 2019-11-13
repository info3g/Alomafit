from django.contrib import admin

from insights.models import *



# Register your models here.


class AdminProduct_Profile_Add_To_Closet(admin.ModelAdmin):
    readonly_fields = ['product', 'customer_profile', ]


class AdminProfile_Try_Product(admin.ModelAdmin):
    readonly_fields = ['product', 'profile', 'try_date', ]


admin.site.register(Profile_Visit_Store)
admin.site.register(HitProduct)
admin.site.register(Product_Profile_Add_To_Closet)
admin.site.register(Profile_Try_Product, AdminProfile_Try_Product)
