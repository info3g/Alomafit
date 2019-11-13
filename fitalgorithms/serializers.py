import sys

from rest_framework import serializers

from customers.model_util import validate_height, validate_weight
from customers.serializers import ProfileSerializer
from fitalgorithms.algorithms import fit_product, full_size, size_range
from insights.models import *
from stores.models import Product
from vfrlight.config import Config as cfg
from vfrlight.util import get_or_raise


class PredictSerializer(serializers.Serializer):
    """
        we could predict the values of the body parts once we have weight and heights

    """

    def update(self, instance, validated_data):
        pass

    height = serializers.IntegerField(default=165, )
    weight = serializers.IntegerField(default=65)
    gender = serializers.ChoiceField([('M', "Male"), ("F", "Female")])
    metric_length = serializers.ChoiceField(choices=(('cm', 'cm'),
                                                     ('in', 'in')),
                                            default='cm')
    metric_weight = serializers.ChoiceField(choices=(('kg', 'kg'),
                                                     ('lb', 'lb')),
                                            default='kg')

    def validate(self, data):
        errors = {'height': validate_height(
            data['height'], data['metric_length'], data['gender']), 'weight': validate_weight(
            data['weight'], data['metric_weight'], data['gender'])}
        for attribute in errors.keys():
            if errors[attribute]:
                raise serializers.ValidationError(errors)
        return data

    def create(self, validated_data):
        print(self)
        print(validated_data)
        sys.stdout.flush()
        # import pdb; pdb.set_trace()
        size = full_size(validated_data['gender'],
                         validated_data['weight'],
                         validated_data['height'],
                         validated_data['metric_weight'],
                         validated_data['metric_length']).get_full_size()
        # in case of Male gender, full size may return size suffixed with long
        size = size.replace('long', '').strip() \
            if validated_data['gender'] == 'M' else size

        size_range_var = size_range(validated_data['gender'][0], size,
                                    validated_data['metric_length'])
        size_range_var.get_range()
        data = size_range_var.__dict__

        return data


def _fit_product(product_id, profile_id):
    """
        Whether we have an authenticated profile or not,
        fitproduct process needs only profile_id and product_id
    """
    product = get_or_raise(Product, shopify_id=product_id)
    profile = get_or_raise(Profile, id=profile_id)
    # first, if we do care about plan then `DONT_CARE_ABOUT_PLAN`==FALSE
    if not cfg.DONT_CARE_ABOUT_PLAN:
        # CHECK if additional values are added in product's variants
        if not product.ready_to_try:
            raise serializers.ValidationError(
                "{} is not ready to try yet :()".format(product.title))
    # second, if we do care about ready_to_try then `DONT_CARE_ABOUT_READY_TO_TRY`==FALSE
    if not cfg.DONT_CARE_ABOUT_READY_TO_TRY:
        # check if product.gender doesn't match the plan
        if not product.covered_by_the_plan:
            raise serializers.ValidationError(
                "{} is not covered by the plan :()".format(product.title))
    '''
        IMPORTANT, we could design a plan scheme,
        Each store could only get only limited number of tries
    '''
    data = fit_product(product=product, profile=profile)

    return data


class Fit_Product_Authenticated_Profile_Serializer(serializers.Serializer):
    product_id = serializers.IntegerField()

    class Meta:
        Model = Profile_Try_Product
        fields = ('product_id',)

    def create(self, validated_data, profile_id):
        product_id = validated_data['product_id']
        return _fit_product(product_id, profile_id)


class Fit_Product_Anonymous_Profile_Serializer(serializers.Serializer):
    profile = ProfileSerializer()
    product_id = serializers.IntegerField()

    class Meta:
        Model = Profile_Try_Product
        fields = ('profile', 'product_id',)

    def create(self, validated_data):
        product_id = validated_data['product_id']
        try:
            '''
            With anonymous profile, please check UNIQUE contraints
            to make sure, there is no duplicated values.
            '''
            profile = get_or_raise(Profile, **validated_data['profile'])
        except:
            # if there is no duplicated values then do create it
            profile = Profile.objects.create(**validated_data['profile'])
        return _fit_product(product_id, profile.id)
