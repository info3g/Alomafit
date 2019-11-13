from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer

from customers.serializers import ProfileSerializer
from insights.models import Profile_Visit_Store, HitProduct, STILL_IN_FITTING_ROOM_TIME_INTERVAL, \
    Product_Profile_Add_To_Closet, Profile_Try_Product
from stores.models import Product
from vfrlight.util import get_or_raise


class Store_Visitor_Serializers(NestedHyperlinkedModelSerializer):
    """
        retrieve all the profiles that visited some store
    """
    profile = ProfileSerializer()

    class Meta:
        model = Profile_Visit_Store
        fields = ('profile',)


class HitProduct_Serializer(HyperlinkedModelSerializer):
    """
        Here we have to keep track of time spent on fitting room
        it called just one time to get a token after that and StillInFittingRoom_Serializer
        will handle the rest.
        It goes like this, first one open the fitting room inside the store front
        a new HitProduct instance have to be instantiated, hence a token will be generated
        and then each time interval specified by the fron-end and back-end will be handled
        by still in room logic
    """
    product = serializers.IntegerField(source='product.shopify_id')

    class Meta:
        model = HitProduct
        fields = ('product', 'token', 'try_duration_seconds')
        read_only_fields = ('token', 'try_duration_seconds',)

    def create(self, validated_data):
        product = get_or_raise(Product, shopify_id=validated_data['product'])
        hitproduct = HitProduct.objects.create(product=product)
        return {'token': hitproduct.token}


class StillInFittingRoom_Serializer(serializers.Serializer):
    '''
        It assumes that HitProduct has been instantiated with the token below
        hence new token will be generated every time we update the time spent
        in the fitting room.
    '''
    token = serializers.CharField(max_length=255)

    def create(self, validated_data):
        token = validated_data['token']
        hitproduct = get_or_raise(HitProduct, token=token)
        hitproduct.try_duration_seconds = hitproduct.try_duration_seconds + \
                                          STILL_IN_FITTING_ROOM_TIME_INTERVAL
        hitproduct.save()
        return {'new token': hitproduct.token,
                'product': hitproduct.product.shopify_id,
                'try duration in seconds': hitproduct.try_duration_seconds}


class Product_Profile_Add_To_Closet_ProductPerspectiveSerializer \
            (NestedHyperlinkedModelSerializer):
    '''
        To list all the profiles that added some product to its closets
        From a product perspective
    '''
    profile = ProfileSerializer()

    class Meta:
        model = Product_Profile_Add_To_Closet
        fields = ('profile',)


class TriedProductsFromProductPerspectiveViewSet \
            (NestedHyperlinkedModelSerializer):
    # to list all the profiles that tried some product with the coressponding try date
    profile = ProfileSerializer()

    class Meta:
        model = Profile_Try_Product
        fields = ('profile', 'try_date')
