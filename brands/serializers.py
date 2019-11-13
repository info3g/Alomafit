from rest_framework.serializers import ModelSerializer

from brands.models import Brand, Size


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        # fields = ('id', 'name', 'gender', 'product_types')
        fields = '__all__'


class ProductTypeSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ('product_types',)


class SizeSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ('sizes',)


class MeasurementsSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ('part', 'measurements')


class UnitSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ('unit',)


class SizeModelSerializer(ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'
