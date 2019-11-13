from datetime import datetime, timedelta

import jwt
from django.db import models

from customers.models import Profile
from vfrlight import settings


class Profile_Visit_Store(models.Model):
    """
        Note here we relate visiting store to profile model, as in the case when an
        Anonymous customer is trying out some product, so the visitin action is bound
        to a profile instance
    """
    store = models.ForeignKey(
        'stores.Store', on_delete=models.CASCADE, related_name='store_visitors')
    profile = models.ForeignKey(
        'customers.Profile', on_delete=models.CASCADE, related_name='profile_visiting')

    class Meta:
        unique_together = (("store", "profile"),)
        ordering = ('store', 'profile',)

    @staticmethod
    def yet_another_store_visitor(store, profile):
        try:
            visited = Profile_Visit_Store.objects.get(store=store, profile=profile)
        except:
            Profile_Visit_Store.objects.create(store=store, profile=profile)


class Product_Profile_Add_To_Closet(models.Model):
    """
        Note here we have two seperate models, `Product_Profile_Add_To_Closet` and
        `Profile_Try_Product`, the former is  only created with logged in customers
        while the latter could be created with Anonymous customers i.e with profile
        whose customer's foreignKey is NULL
    """
    product = models.ForeignKey(
        'stores.Product', on_delete=models.CASCADE, related_name='product_added_to_closet')
    customer_profile = models.ForeignKey(
        'customers.Profile', on_delete=models.CASCADE, related_name='profile_add_to_closet')

    class Meta:
        unique_together = (("product", "customer_profile"),)
        ordering = ('product',)

    @staticmethod
    def yet_another_added_to_closet_action(profile, product):
        created = False
        try:
            obj = Product_Profile_Add_To_Closet.objects.get(product=product,
                                                            customer_profile=profile)
        except:
            obj = Product_Profile_Add_To_Closet.objects.create(product=product,
                                                               customer_profile=profile)
            created = True
        return obj, created

    def __str__(self):
        return "profile: {} added {} ".format(self.customer_profile, self.product)


class Profile_Try_Product(models.Model):
    product = models.ForeignKey(
        'stores.Product', on_delete=models.CASCADE, related_name='product_tried')
    profile = models.ForeignKey(
        'customers.Profile', on_delete=models.CASCADE, related_name='profile_try')
    try_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            ("product", "profile", "try_date"),)
        ordering = ('product', 'profile',)


# the life time after generating token in HitProduct instance
VALID_TOKEN_HIT_PRODUCT_DURATION_SECONDS = 3600
'''
    front-end should inform the server every one minute for example,
    to update time that spent since hit button has been hit
'''
STILL_IN_FITTING_ROOM_TIME_INTERVAL = 60


class HitProduct(models.Model):
    """
        This Model define a short term living instance.
        When a hit_product is instatiated, try_duration_seconds will be updated
        with timer request scheme, until it's token is not valid, which would be
        the case after VALID_TOKEN_HIT_PRODUCT_DURATION_SECONDS,
        token is always unique, because we are setting each one with a unique exp value

        Note here once a new record is created, current time will be set as try_data
        Value and a 1 minute for try_duration_minutes,
        TODO: an api for updating try_duration_minutes every minute the profile is
        still seeing the vector image is required
    """
    token = models.CharField(
        max_length=255, unique=True)
    product = models.ForeignKey(
        'stores.Product', on_delete=models.CASCADE, related_name='product_hit')
    try_duration_seconds = models.IntegerField(default=60)

    class Meta:
        unique_together = (
            ("token", "product"),)
        ordering = ('product', 'try_duration_seconds', 'token')

    def update(self, *args, **kwargs):
        # TODO if((datetime.now()- (decoded old token).exp)<0): revoke update
        super().update(*args, **kwargs)

    def save(self, *args, **kwargs):
        dt = datetime.now() + timedelta(seconds=VALID_TOKEN_HIT_PRODUCT_DURATION_SECONDS)
        token = jwt.encode({
            'id': self.product.shopify_id,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')
        self.token = token.decode('utf-8')
        super(HitProduct, self).save(*args, **kwargs)
