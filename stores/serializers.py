import shopify
from rest_framework import serializers
from rest_framework.serializers import (HyperlinkedModelSerializer,
                                        ValidationError)
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer

from stores.models import *
from theming.serializers import ThemeSerializer
from vfrlight.util import get_or_raise, initialize


class VariantSerializer(HyperlinkedModelSerializer):
    hips = serializers.FloatField(allow_null=True, required=False)
    waist = serializers.FloatField(allow_null=True, required=False)
    bust = serializers.FloatField(allow_null=True, required=False)
    shoulder = serializers.FloatField(allow_null=True, required=False)

    class Meta:
        model = Variant
        fields = ('shopify_id', 'title', 'hips',
                  'waist', 'bust', 'shoulder', 'position')
        read_only_fields = ('shopify_id', 'title', 'position')


class ProductSerializer(NestedHyperlinkedModelSerializer):
    # variants = VariantSerializer(many=True)
    parent_lookup_kwargs = {
        'url': 'url',
    }

    # locale = serializers.SerializerMethodField()
    # cm_or_in = serializers.SerializerMethodField()
    # kg_or_lb = serializers.SerializerMethodField()

    @staticmethod
    def get_cm_or_in(instance):
        return instance.store.cm_or_in

    @staticmethod
    def get_kg_or_lb(instance):
        return instance.store.kg_or_lb

    @staticmethod
    def get_locale(instance: Product):
        return instance.store.primary_locale

    def validate(self, data):

        def validate_required_attributes(variant, required_attributes):
            errors = {}
            for attribute in required_attributes:
                if variant.get(attribute, None) is None:
                    errors[attribute] = "{}: is required, please fill it".format(
                        attribute)
            if len(errors.keys()) > 0:
                return None  # return erross
            return None

        def validate_non_required_attributes(variant, required_attributes):
            errors = {}
            not_required_attributes = list(set(body_parts_list)
                                           .difference(set(required_attributes)))
            for attribute in not_required_attributes:
                if variant.get(attribute, None) is not None:
                    errors[attribute] = (
                        "{} is NOT required, please don't fill it").format(attribute)
            if len(errors.keys()) > 0:
                return None  # return errors
            return None

        errors = {}
        productType = self.__dict__['_kwargs']['data']['product_type']
        required_attributes = from_product_type_to_required_body_parts(
            productType, self.__dict__['_kwargs']['data']['gender'])
        for i, variant in enumerate(data['variants']):
            variantName = "variant {}".format(i + 1)
            errors[variantName] = {}
            errors[variantName]['required_attributes'] = validate_required_attributes(
                variant, required_attributes)
            errors[variantName]['non_required_attributes'] = validate_non_required_attributes(
                variant, required_attributes)
            errors[variantName]['bust'] = validate_variant_range(
                data['gender'], 'bust',
                variant.get(
                    'bust', None), VariantRangesDict.product_ranges['bust'],
                metric=data['metric'], is_person=False)
            errors[variantName]['waist'] = validate_variant_range(
                data['gender'], 'waist',
                variant.get(
                    'waist', None), VariantRangesDict.product_ranges['waist'],
                metric=data['metric'], is_person=False)
            errors[variantName]['hips'] = validate_variant_range(
                data['gender'], 'hips',
                variant.get(
                    'hips', None), VariantRangesDict.product_ranges['hips'],
                metric=data['metric'], is_person=False)
            errors[variantName]['shoulder'] = validate_variant_range(
                data['gender'], 'shoulder',
                variant.get(
                    'shoulder', None), VariantRangesDict.product_ranges['shoulder'],
                metric=data['metric'], is_person=False)

        for variant_errors in errors.keys():
            for error in errors[variant_errors].keys():
                if not errors[variant_errors][error] is None:
                    raise serializers.ValidationError(errors)
        return data

    class Meta:
        model = Product
        # fields = ('shopify_id', 'title', 'product_type',
        #           'gender', 'image', 'variants',
        #           'updated_at', 'available_online', 'created_at',
        #           'vendor', 'elasticity', 'fabric', 'fit_type',
        #           'times_tried', '_required_attributes',
        #           'ready_to_try', 'covered_by_the_plan',
        #           'metric', 'locale', 'denim', 'one_size', 'kg_or_lb', 'cm_or_in')

        fields = ('title', 'created_at', 'product_type',
                  'vendor', 'gender', 'image')
        read_only_fields = ('title', 'created_at',
                            'product_type', 'vendor', 'gender', 'image')

        # read_only_fields = ('shopify_id', 'title',
        #                     'image', 'updated_at', 'available_online',
        #                     'created_at', 'vendor', 'times_tried',
        #                     '_required_attributes', 'ready_to_try',
        #                     'covered_by_the_plan', 'locale', 'kg_or_lb', 'cm_or_in')

    def update(self, instance, validated_data):
        variants_data = validated_data.pop('variants')

        instance.product_type = validated_data.get(
            'product_type', instance.product_type)
        instance.gender = validated_data.get('gender', instance.title)
        instance.updated_at = datetime.now()
        instance.elasticity = validated_data.get(
            'elasticity', instance.elasticity)
        instance.fabric = validated_data.get(
            'fabric', instance.fabric)
        instance.fit_type = validated_data.get(
            'fit_type', instance.fit_type)
        instance.metric = validated_data.get(
            'metric', instance.fit_type)
        instance.denim = validated_data.get(
            'denim', instance.denim)
        instance.one_size = validated_data.get(
            'one_size', instance.one_size)
        instance.save()

        variants = instance.variants.all()
        variants = list(variants)

        for variant_data in variants_data:
            variant = variants.pop(0)
            variant.shoulder = variant_data.get(
                'shoulder', variant.shoulder)
            variant.bust = variant_data.get('bust', variant.bust)
            variant.waist = variant_data.get('waist', variant.waist)
            variant.hips = variant_data.get('hips', variant.hips)

            variant.save()
        return instance


class StoreSerializer(HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.user.username')
    lookup_field = 'slug'
    most_added_to_closet = serializers.ReadOnlyField()
    extra_kwargs = {
        'slug': {'lookup_field': 'slug'}
    }
    activated_plan = serializers.SerializerMethodField()
    free_trial_left = serializers.SerializerMethodField()
    theme = ThemeSerializer(read_only=True)

    @staticmethod
    def get_activated_plan(store):
        for p in store.plans:
            if store.plans[p]:
                return p
        return None

    @staticmethod
    def get_free_trial_left(store):
        return store.free_trial_left()

    class Meta:
        model = Store
        fields = ('url', 'plans', 'owner', 'slug', 'male_body_shapes',
                  'female_body_shapes', 'male_top_sizes',
                  'male_bottom_sizes', 'female_top_sizes',
                  'female_bottom_sizes', 'most_added_to_closet',
                  'average_hit_duration', 'cm_or_in', 'kg_or_lb', 'tries_this_billing_cycle', 'tries_left',
                  'activated_plan', 'free_trial_left', 'theme')
        read_only_fields = ('url', 'plans', 'male_body_shapes',
                            'female_body_shapes', 'male_top_sizes',
                            'male_bottom_sizes', 'female_top_sizes',
                            'female_bottom_sizes', 'most_added_to_closet',
                            'average_hit_duration', 'tries_this_billing_cycle', 'tries_left', 'activated_plan',
                            'free_trial_left')


class MerchantSerializer(serializers.ModelSerializer):
    store = serializers.PrimaryKeyRelatedField(read_only=True)
    queryset = Merchant.objects.all()

    class Meta:
        model = Merchant
        fields = ('user', 'store',)


class NonAuthenticatedGetProduct(serializers.Serializer):
    pk = serializers.IntegerField(required=True)
    store_slug = serializers.SlugField(required=True)

    def validate(self, data):
        store = get_or_raise(Store, slug=data['store_slug'])
        product = get_or_raise(Product, shopify_id=data['pk'])

        if not product.store == store:
            raise ValidationError(
                "{} does not belong to {}".format(product.title, store.url))
        return data


class SyncSerializer(serializers.Serializer):

    def create(self, validated_data, store, missing_brands):
        store, merchant_token = initialize(
            token=store.token, shop=store.url, source="sync")
        return {'store': store.url, 'token': merchant_token, 'missing_brands': missing_brands}


class ActivatePlanSerializer(serializers.Serializer):
    plan = serializers.ChoiceField(
        choices=plans.choices + [[x, x] for x in ['Male', 'Female', 'MaleAndFemale']])

    def create(self, validated_data, store):
        shopify.ShopifyResource.clear_session()
        with shopify.Session.temp(store.url, store.token):
            test_charge = cfg.DEBUG
            plan = validated_data['plan']
            if len(plan.split(" ")) == 1:
                plan = plan + " Second"
            # check if the store is from our DEVELOPMENT_STORES
            if store.url in cfg.DEVELOPMENT_STORES:
                # fake billing
                test_charge = True
            if plan.split(" ")[1] == "Free":
                store.activate_plan(plan)
                return store.free_trial_left()
            else:
                recur_charge = shopify.RecurringApplicationCharge({
                    "name": plan,
                    "price": RecurringCharge.billing_amount(plan),
                    "return_url": cfg.SHOPIFY_CONFIG['CHARGES_RETURN_URL'],
                    "trial_days": 0,
                    "test": test_charge
                })
                recur_charge.save()
                RecurringCharge.objects.create(shopify_id=recur_charge.attributes['id'],
                                               status=recur_charge.attributes['status'],
                                               plan=plan,
                                               store=store)
                return recur_charge.attributes['confirmation_url']
