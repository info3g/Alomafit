from allauth.account.forms import ResetPasswordForm
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import PasswordResetSerializer
from rest_framework import serializers, validators
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer

from customers.models import *
from insights.models import Product_Profile_Add_To_Closet, Profile_Try_Product
from stores.model_util import VariantRangesDict, validate_variant_range
from stores.models import Product
from stores.serializers import ProductSerializer
from vfrlight.util import get_or_raise


class Product_Profile_Add_To_Closet_ProfilePerspectiveSerializer(NestedHyperlinkedModelSerializer):
    """
        profile can add many products to its closet, while also product could be added
        by many profiles, so we have two options to serialize
            1)  when we are on the view of the product data and we want to see who added
                this product to its closet
            2)  when we are on the view of the profile data and we want to see which
                products are added to his closet

    """
    product_data = ProductSerializer(read_only=True)
    product = serializers.IntegerField()

    def validate(self, data):
        # first get profile and product
        product_id = data['product']
        self.context['profile'] = get_or_raise(
            Profile, id=self.context['profile_id'])
        self.context['product'] = get_or_raise(
            Product, shopify_id=product_id)
        try:
            # if they are not existed, i.e profile has not added the product,
            # to his closet, Validation is True
            obj = Product_Profile_Add_To_Closet.objects.get(
                product=self.context['product'],
                customer_profile=self.context['profile'])
        except:
            return data
        # if no exception has fired, that means it's already existed
        raise serializers.ValidationError("{} has added {} to his closet".
                                          format(self.context['profile'],
                                                 self.context['product']))

    def create(self, validated_data):
        Product_Profile_Add_To_Closet.objects.create(
            product=self.context['product'],
            customer_profile=self.context['profile'])

    class Meta:
        model = Product_Profile_Add_To_Closet
        fields = ('product', 'product_data')
        read_only_fields = ('product_data',)


class TriedProductsProfilePerspectiveSerializer(NestedHyperlinkedModelSerializer):
    """
        This serializer works as information source,
        history of the profile actions is necessary
    """
    product = serializers.ReadOnlyField(source='product.shopify_id')

    class Meta:
        model = Profile_Try_Product
        fields = ('product', 'try_date')


class ProfileSerializer(NestedHyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'name', 'height', 'weight', 'bust', 'waist',
                  'shoulder', 'hips', 'gender', 'metric_length',
                  'metric_weight', 'body_shape',
                  'top_size', 'bottom_size', 'skin')
        read_only_fields = ('id', 'body_shape',
                            'top_size', 'bottom_size')

    def validate(self, data):
        errors = {}
        errors['height'] = validate_height(height=data['height'],
                                           metric_length=data['metric_length'],
                                           gender=data['gender'])
        errors['weight'] = validate_weight(weight=data['weight'],
                                           metric_weight=data['metric_weight'],
                                           gender=data['gender'])
        # validate all the fields of body measurements
        errors['bust'] = validate_variant_range(
            data['gender'], 'bust', data['bust'], VariantRangesDict.profile_ranges['bust'],
            metric=data['metric_length'], is_person=True)
        errors['waist'] = validate_variant_range(
            data['gender'], 'waist', data['waist'], VariantRangesDict.profile_ranges['waist'],
            metric=data['metric_length'], is_person=True)
        errors['hips'] = validate_variant_range(
            data['gender'], 'hips', data['hips'], VariantRangesDict.profile_ranges['hips'],
            metric=data['metric_length'], is_person=True)
        errors['shoulder'] = validate_variant_range(
            data['gender'], 'shoulder', data['shoulder'], VariantRangesDict.profile_ranges['shoulder'],
            metric=data['metric_length'], is_person=True)

        # if any error occurred, raise a validation error with json response
        errors = {key: value for key, value in errors.items() if not (value is None)}
        if len(errors.keys()) > 0:
            raise serializers.ValidationError(errors)
        return data

    def update(self, validated_data, profile):
        profile.update(**validated_data)
        for obj in profile.all():
            obj.save()

    def create(self, validated_data, customer=None):
        Profile.objects.create(
            customer=customer, **validated_data)

    def run_validators(self, value):
        """
            we remove the UniqueTogetherValidator validater for
            the sake of populating our database
        """
        for validator in self.validators:
            if isinstance(validator, validators.UniqueTogetherValidator):
                self.validators.remove(validator)
        super(ProfileSerializer, self).run_validators(value)


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    queryset = Customer.objects.all()
    lookup_field = 'slug'
    id = serializers.ReadOnlyField(source='user.id')
    # here we use nested router to list profile views under specific customer view
    extra_kwargs = {
        'slug': {'lookup_field': 'slug'}
    }

    class Meta:
        model = Customer
        fields = ('slug', 'id')


class PasswordSerializer(PasswordResetSerializer):
    password_reset_form_class = ResetPasswordForm


class CustomerRegisterSerializer(RegisterSerializer):
    """
        we override the RegisterSerializer, hence we replace it in
        the settings file, to create a customer instance and bind it to
        the newly created user, the api /registration
    """

    def save(self, *args, **kwargs):
        user = super(CustomerRegisterSerializer,
                     self).save(*args, **kwargs)
        customer = Customer.objects.create(user=user)
        return user
