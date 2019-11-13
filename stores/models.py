import re
from datetime import datetime, timedelta

import dateutil.parser
from django.conf import settings
from django.contrib.postgres.fields import ArrayField, JSONField
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

from customers.models import (bodyBottomSizeListFemale, bodyBottomSizeListMale,
                              bodyShapeList, bodyTopSizeListFemale,
                              bodyTopSizeListMale)
from fitalgorithms.utility_helper import in_to_cm
from insights.models import (HitProduct, Product_Profile_Add_To_Closet,
                             Profile_Try_Product, Profile_Visit_Store)
from stores.model_util import *
from vfrlight.config import Config as cfg


class Merchant(models.Model):
    """
        To support Authentication with the store, for any api requires
        updating the store's data, a user account must be bound to the store
        Here we are assigning user to merchant via OneToOne relationship
        So we could generate token, and use Token Based authentication scheme
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='merchant_user')


class Store(models.Model):
    """
        The store model is the corner stone of our app
    """
    # each store is owned by an owner
    owner = models.OneToOneField(
        Merchant,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='merchant_store')
    # and has its unique domain name i.e URL
    url = models.CharField(
        unique=True, max_length=255, editable=False)
    # we slugify the url to use it in routing, please see stores.urls.py
    slug = models.SlugField(
        unique=True, max_length=255, editable=False)
    '''
        We use the `JWT` implementation, Json Web Token, to authenticate with store API
        Hence, any one could access our app must authenticate first with shopify then
        we have a merchant account bounded to the store and from here we generate Token
        to let front-end client authenticate with us for any Update operations
    '''
    token = models.CharField(
        max_length=32, editable=True, default="0")
    '''
        each store has some plan to be enabled, if there is not any,
        then his fitting room on the store front is locked
    '''
    plans = JSONField(
        default={plan: None for plan in plans.listOfChoices})
    '''
        we use this boolean field as an indicator whether the store
        has registered all the webhooks and script tag
    '''

    cm_or_in = models.TextField(
        max_length=2,
        choices=(('cm', 'CM'),
                 ('in', 'INCH')),
        default='cm')

    kg_or_lb = models.TextField(
        max_length=2,
        choices=(('kg', 'Kilogram'),
                 ('lb', 'Pound')),
        default='kg')

    webhooks_added = models.BooleanField(default=False)
    '''
        just for clarification, we add JavaScript code to the store front on shopify
        the purpose of it, is to check if its a product page the inject the fitting room
        and add the try-on button
    '''
    scripttag_added = models.BooleanField(default=False)
    '''
        Those statistics are collected to project them on the dashboard
        Hence we have such models [1] specific for saving those values but
        we don't need to run to many queries.
        [1] Profile_Visit_Store

        As for profile: after its values being filled, bodyShape will be evaluated
        as well ass top_size and bottom_size.
        Instead of quering thoses values from the Profile_Visit_Store `manyTomany`
        relationship we saved for each store explicitly

    '''
    bodyShape_dict = {bodyShape: 0 for bodyShape in bodyShapeList}
    male_body_shapes = JSONField(default=bodyShape_dict)
    female_body_shapes = JSONField(default=bodyShape_dict)

    MaleTopBodySize_dict = {bodySize: 0 for bodySize in
                            bodyTopSizeListMale}
    MaleBottomBodySize_dict = {bodySize: 0 for bodySize in
                               bodyBottomSizeListMale}
    # Although they both derive from the same list but no harm in that
    FemaleTopBodySize_dict = {bodySize: 0 for bodySize in
                              bodyTopSizeListFemale}
    FemaleBottomBodySize_dict = {bodySize: 0 for bodySize in
                                 bodyBottomSizeListFemale}

    male_top_sizes = JSONField(default=MaleTopBodySize_dict)
    male_bottom_sizes = JSONField(default=MaleBottomBodySize_dict)

    female_top_sizes = JSONField(default=FemaleTopBodySize_dict)
    female_bottom_sizes = JSONField(default=FemaleTopBodySize_dict)

    first_install = models.DateTimeField(default=timezone.now)

    primary_locale = models.TextField(default="None")

    did_fetch_data_during_connect = models.BooleanField(default=False)

    tries_this_billing_cycle = models.IntegerField(default=0)

    plan_last_activated_on = models.DateField(null=True, default=None)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.url)
        '''
            save the time the admin has installed our app for the first time,
            it's actually quite helpful for setting new free trial period in case
            of admin reinstalled our app and wants to upgrade to some plan
        '''
        super(Store, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    class Meta:
        ordering = ('url',)

    def activate_plan(self, plan):
        self.deactivate_any_plan()
        self.plans[plan] = True
        self.plan_last_activated_on = timezone.now()
        self.save()

    def set_primary_locale(self, primary_locale):
        self.primary_locale = primary_locale
        self.save()

    def deactivate_any_plan(self):
        for key in self.plans.keys():
            self.plans[key] = None
        self.save()

    def reset_webhooks(self):
        self.webhooks_added = False
        self.save()

    def reset_scriptt_ags(self):
        self.scripttag_added = False
        self.save()

    def register_webhooks(self):
        self.webhooks_added = True
        self.save()

    def register_script_tags(self):
        self.scripttag_added = True
        self.save()

    @property
    def average_hit_duration(self):
        # Just group by product and order their hit durations in a descending order
        products_store_ids = list(self.products.all().
                                  values_list('shopify_id', flat=True))

        average_hit_duration_result = HitProduct.objects.all() \
            .filter(product__in=products_store_ids) \
            .values('product_id') \
            .annotate(average_duration=models.Avg('try_duration_seconds')) \
            .order_by('-average_duration')

        return average_hit_duration_result

    @property
    def most_added_to_closet(self):
        """
            just group by product and accumlate how many times each
            product has been added to someone closet.
        """
        products_store_ids = list(self.products.all().
                                  values_list('shopify_id', flat=True))
        most_added_to_closet_result = Product_Profile_Add_To_Closet.objects.all() \
            .filter(product__in=products_store_ids) \
            .values('product_id') \
            .annotate(count=models.Count('product_id')) \
            .order_by('-count')

        return most_added_to_closet_result

    def increase_tries(self):
        self.tries_this_billing_cycle += 1
        self.save()

    def check_and_update_tries(self):
        if self.plan_last_activated_on is not None:
            if (datetime.date(timezone.now()) - self.plan_last_activated_on).days >= 30:
                self.plan_last_activated_on = self.plan_last_activated_on + timedelta(days=30)
                self.tries_this_billing_cycle = 0
                self.save()

    @property
    def tries_left(self):
        self.check_and_update_tries()
        plan = None
        for p in self.plans:
            if self.plans[p] is not None:
                plan = p
        if plan is None:
            return 0
        return cfg.PLANS[plan.split(" ")[0]][plan.split(" ")[1]]["Tries"] - self.tries_this_billing_cycle

    def yet_another_visitor(self, profile):
        """
            Every time some authenticated/non authenticated profile has tried some product
            Visiting action has occured. just save this info
        """
        if profile.gender.lower() == 'm':
            self._yet_another_male_visitor(profile)
        else:
            self._yet_another_female_visitor(profile)
        Profile_Visit_Store.yet_another_store_visitor(
            store=self, profile=profile)
        self.save()

    # accumlate statistics for male profile
    def _yet_another_male_visitor(self, profile):
        self.male_top_sizes[profile.top_size] = \
            self.male_top_sizes[profile.top_size] + 1
        self.male_bottom_sizes[profile.bottom_size] = \
            self.male_bottom_sizes[profile.bottom_size] + 1
        self.male_body_shapes[profile.body_shape] = \
            self.male_body_shapes[profile.body_shape] + 1

    # accumlate statistics for female profile
    def _yet_another_female_visitor(self, profile):
        self.female_top_sizes[profile.top_size] = \
            self.female_top_sizes[profile.top_size] + 1
        self.female_bottom_sizes[profile.bottom_size] = \
            self.female_bottom_sizes[profile.bottom_size] + 1
        self.female_body_shapes[profile.body_shape] = \
            self.female_body_shapes[profile.body_shape] + 1

    '''
        In a scenario where admin has reinstalled our app, compare between
        the first time that installed our app to see how many free trial days left
    '''

    def free_trial_left(self):
        now = datetime.now()
        timediff = (now - self.first_install.replace(tzinfo=None)).days
        return cfg.FREE_TRIAL - timediff


#
# (Chest ,Waist  , Hips) for male
# (Bust , waist  , hips) for female
# and weight + height for all
# you can use chest and bust as one field


class ProductShopifyManager(models.Manager):

    def get_image_src(self, shopify_product):
        if len(shopify_product.images):
            src_image = shopify_product.images[0].src
        else:
            src_image = \
                'https://help.shopify.com/assets/shopify-full-color-black.svg'
        return src_image

    def get_product_type(self, shopify_product):
        product_type = shopify_product.product_type.lower()
        if product_type not in ProductTypeChoicesList:
            product_type = ProductTypeChoicesList[0]
        return product_type

    # def get_product_type(self, shopify_product):
    #     product_type = shopify_product.product_type.lower() \
    #         if shopify_product.product_type.lower() \
    #            in ProductTypeChoicesList \
    #         else ProductTypeChoicesList[0]
    #     return product_type

    '''
        For Product model we have customer ObjectManage to handle the
        update process from shopify, such as vendor,image,update/create date
        Hence we pass shopify_product data and we expect to update the model instance
        right from it
    '''

    def assign_values(self, shopify_product):
        obj_data_ = {}
        obj_data_['title'] = shopify_product.title
        obj_data_['handle'] = shopify_product.handle
        upat = dateutil.parser.parse(shopify_product.updated_at)
        obj_data_['updated_at'] = \
            upat if upat is not None \
                else datetime.now()
        # obj_data_['product_type'] = \
        #     self.get_product_type(shopify_product) if self.get_product_type(shopify_product) is not None \
        #         else 'top'
        obj_data_['product_type'] = self.get_product_type(shopify_product)
        obj_data_['available_online'] = \
            True if shopify_product.published_at is not None \
                else False
        # obj_data_['vendor'] = shopify_product.vendor
        obj_data_['vendor'] = \
            shopify_product.vendor if shopify_product.vendor is not None \
                else ' '

        crat = dateutil.parser.parse(shopify_product.created_at)
        obj_data_['created_at'] = \
            crat if crat is not None \
                else datetime.now()
        img = self.get_image_src(shopify_product)

        obj_data_['image'] = \
            img if img is not None \
                else ''

        return obj_data_

    def equal(self, shopify_product, db_product):
        """
            Here we check the equality between shopfiy backend and ours, to
            see if it's necessary to update our database
        """
        all_true_list = []
        all_true_list.append(shopify_product.title == db_product.title)
        all_true_list.append((shopify_product.published_at is not None) ==
                             db_product.available_online)
        all_true_list.append(shopify_product.vendor == db_product.vendor)
        all_true_list.append(self.get_image_src(
            shopify_product) == db_product.image)
        all_true_list.append(self.get_product_type(
            shopify_product) == db_product.product_type)

        # all the constraints must be satisfied
        if False in all_true_list:
            return False
        del all_true_list
        variants_db_dict = {v.shopify_id: v for v in db_product.variants.all()}
        # As for variants, all we need is the position as well as the title
        for variant in shopify_product.variants:
            variant_db = variants_db_dict[variant.id]
            b1 = variant.title == variant_db.title
            b2 = variant.position == variant_db.position
            if not (b1 and b2):
                return False
        return True

    def create_from_shopify(self, store, shopify_product):
        # from django.core.mail import send_mail
        # from vfrlight.settings import EMAIL_HOST_USER
        # import sys
        """
            Just create a new instance with shopify product data, hence variants data
            are embedded inside the product data as nested field
            we also assign the store the product comes from.
        """
        obj_data = self.assign_values(shopify_product)
        obj_data['store'] = store
        obj_data['shopify_id'] = shopify_product.id
        # product_type = obj_data["product_type"]
        # obj_data["product_type"] = "shirts"
        # send_mail(
        #     "Welcome to create_from_shopify",
        #     "Hello product_type: " + str(product_type) + " obj_data " + str(obj_data),
        #     EMAIL_HOST_USER,
        #     ["surinder.indybytes@gmail.com"],
        #     fail_silently=True,
        # )
        product = super().create(**obj_data)
        for variant in shopify_product.variants:
            Variant.Shopify_objects.create_from_shopify(
                shopify_variant=variant, product=product).save()
        return product

    def update_from_shopify(self, shopify_product):
        # update from shopify, just get product shopify_id and update the fileds accordingly
        obj_data = self.assign_values(shopify_product)
        queryset = super().filter(pk=shopify_product.id)
        if not queryset.all()[0].product_type == 'None':
            # this queryset operations is just for the sake of `update`
            if obj_data['product_type'] == 'None':
                # to make sure that product type does not set to its default value, None
                obj_data['product_type'] = queryset.all()[0].product_type
        updated_product = queryset.update(**obj_data)
        # update doesn't call save method, so we explicitly call it
        for obj in queryset.all():
            obj.save()
        for variant in shopify_product.variants:
            Variant.Shopify_objects.update(
                shopify_variant=variant)
        return updated_product


class Product(models.Model):
    # shopify attributes
    shopify_id = models.BigIntegerField(primary_key=True, editable=False)
    # title of product
    title = models.TextField(default='no title', blank=False)
    # Image Url
    image = models.URLField()
    # name of the comany that made that product
    vendor = models.CharField(null=True, max_length=40)
    available_online = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    # product only belongs to one and only one store

    handle = models.TextField(default="")  # handle is used to know the link of product

    store = models.ForeignKey('stores.Store', on_delete=models.CASCADE, related_name='products', editable=False)
    # for fit algorithm,
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), default='M')
    # all the fields below are clarified extensively
    product_type = models.CharField(max_length=productType.max_length, choices=productType.choices,
                                    default=productType.listOfChoices[0])
    fit_type = models.CharField(max_length=product_fit_Type.max_length, choices=product_fit_Type.choices,
                                default=product_fit_Type.listOfChoices[0])
    elasticity = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    fabric = models.CharField(max_length=fabricType.max_length, choices=fabricType.choices,
                              default=fabricType.listOfChoices[0])

    # Added By Nour Alhadi (If any error remove this block)
    denim = models.BooleanField(default=False)
    one_size = models.BooleanField(default=False)
    # Finished Addition

    # solely used for insight purposes

    times_tried = models.IntegerField(default=0)
    '''
        since we admins don't need to fill any non required data specified by
        the product type, hence we allow only those fields hips/bust/shoulder/waist
        to be filled if and only if those are really required, i.e in case of
        jeans product type we don't needs shoulder value to be filled in any of the
        variants of the product
    '''
    _required_attributes = ArrayField(
        models.CharField(max_length=body_parts_choiceField.max_length, choices=body_parts_choiceField.choices,
                         null=False))
    # here we first set objects to be the default manager, Django require that
    objects = models.Manager()
    # after that we are setting our customer manager
    Shopify_objects = ProductShopifyManager()

    metric = models.CharField(max_length=2, choices=(('cm', 'cm'), ('in', 'in')), default='cm')
    active = models.NullBooleanField(null=True)

    class Meta:
        ordering = ('title',)

    def save(self, *args, **kwargs):
        self._required_attributes = from_product_type_to_required_body_parts(
            self.product_type, self.gender)
        '''
           Since we allow the product type to be changed,
           Any required attributes that become non required, all of its variants
           values should be set to a None value
        '''
        for variant in self.variants.all():
            non_required_attributes = set(body_parts_list).difference(
                set(self._required_attributes))
            for non_required_attribute in non_required_attributes:
                variant.__dict__[non_required_attribute] = None
            variant.save()
        super(Product, self).save(*args, **kwargs)

    def original_save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def covered_by_the_plan(self):
        """
            it's very straightforward, if product's gender matches the plan
            and number of tries is less than monthly available
            then it's covered
        """
        does_plan_match = False
        are_tries_available = False
        regex_male = re.compile(r"^Male.*$")
        regex_female = re.compile(r"^Female.*$")
        regex_male_and_female = re.compile(r"^MaleAndFemale.*$")
        if self.gender == 'M':
            for plan in plans.listOfChoices:
                if self.store.plans[plan] and (regex_male.match(plan) or regex_male_and_female.match(plan)):
                    does_plan_match = True
                    break
        elif self.gender == 'F':
            for plan in plans.listOfChoices:
                if self.store.plans[plan] and (regex_female.match(plan) or regex_male_and_female.match(plan)):
                    does_plan_match = True
                    break
        if does_plan_match:
            are_tries_available = self.store.tries_left > 0
        return does_plan_match and are_tries_available

    @property
    def ready_to_try(self):
        """
            if all of product's variants are filled completely, i.e each required
            attributes has some validated value `Non Null` we are allowing this product
            to be tried in the fitting room
        """
        if self.product_type == 'None' or self.fit_type == 'None':
            return False
        for variant in self.variants.all():
            if not variant.ready_to_try():
                return False
        return True

    def yet_another_try(self, profile):
        # just accumulate how many time this product has been tried.
        self.times_tried = self.times_tried + 1
        self.store.increase_tries()
        Profile_Try_Product.objects.create(product=self, profile=profile)
        self.save()

    def yet_added_to_his_closet(self, profile):
        return Product_Profile_Add_To_Closet. \
            yet_another_added_to_closet_action(product=self,
                                               profile=profile)


class VariantShopifyManager(models.Manager):
    """
        please see ProductShopifyManager, the same logic goes here and there
    """

    def assign_values(self, shopify_variant):
        obj_data_ = {}
        obj_data_['title'] = shopify_variant.title
        obj_data_['position'] = shopify_variant.position
        return obj_data_

    def create_from_shopify(self, product, shopify_variant):
        obj_data = self.assign_values(shopify_variant)
        obj_data['product'] = product
        obj_data['shopify_id'] = shopify_variant.id
        obj_data['position'] = shopify_variant.position
        return super().create(**obj_data)

    def update(self, shopify_variant):
        obj_data = self.assign_values(shopify_variant)
        return super().filter(pk=shopify_variant.id).update(**obj_data)


class Variant(models.Model):
    """
        each product could have many variants but, each variant could belong only to
        one product, there is some important attributes such as
        waist,shoulder,hips, etc...  to be filled by the admin
        hence we specify which are required based on the product type
    """
    shopify_id = models.BigIntegerField(
        primary_key=True, editable=False)
    # TODO make sure that title on shopify is not above 40 character length
    title = models.CharField(blank=True, max_length=40)
    product = models.ForeignKey(
        'stores.Product', on_delete=models.CASCADE, related_name='variants', editable=False)

    shoulder = models.FloatField(null=True)
    bust = models.FloatField(null=True)

    waist = models.FloatField(null=True)
    hips = models.FloatField(null=True)
    objects = models.Manager()
    Shopify_objects = VariantShopifyManager()
    '''
        On shopify Admin Dashboard, admin can use drag&drop to alter variants
        positions to be presented in product admin page and store front page
        so we keep track of each position to perserve the same order as specified
        by admins, Note that order is important because we want to show upper,lower
        best fit variant in stress_map.
    '''
    position = models.IntegerField(null=True)

    def __str__(self):
        return self.title

    def ready_to_try(self):
        '''
            variant is ready to try if the required attributes are completely filled
            i.e not null values, put it in another way validated data is saved in the insance
        '''
        for attribute in self.product._required_attributes:
            if (getattr(self, attribute) is None):
                return False
        return True

    @staticmethod
    def group_variants(variants):
        '''
            this method is simple enough to be explained
            just in the fitalgorithm fit_sys method expect lists forms

            variants: are just multi size options of the product.
        '''
        sizes, busts, hips, shoulders, waists = [], [], [], [], []
        # notice here, this ordering operation is a MUST operation
        variants = variants.order_by('position')
        for variant in variants:
            sizes.append(variant.title)
            busts.append(variant.bust)
            hips.append(variant.hips)
            shoulders.append(variant.shoulder)
            waists.append(variant.waist)
        # just grab any variant and infer the product metric...
        if (variant.product.metric == 'in'):
            busts = [in_to_cm(bust) for bust in busts]
            hips = [in_to_cm(hip) for hip in hips]
            shoulders = [in_to_cm(shoulder) for shoulder in shoulders]
            waists = [in_to_cm(waist) for waist in waists]
        return (sizes, busts, hips, shoulders, waists)


class Collection(models.Model):
    '''
        We fetch the gender info for the product from the collection
        resource on shopify, each admin classify his products into collections
        Hence we see if there is any Woman/Man names for collections
        and assign their products accordingly
    '''
    shopify_id = models.BigIntegerField(
        primary_key=True, editable=False)
    title = models.CharField(blank=True, max_length=40)
    gender = models.CharField(
        max_length=1,
        choices=(('M', 'Male'),
                 ('F', 'Female'),
                 ('N', 'None, this collection is not talking about gender')),
        default='N')

    @staticmethod
    def gender_converter(collection_title):
        if (collection_title.lower() == 'women'):
            return 'F'
        elif (collection_title.lower() == 'men'):
            return 'M'
        else:
            return 'N'

    def save(self, *args, **kwargs):
        if self.title.lower() in collection_gender_list:
            self.gender = Collection.gender_converter(self.title)
        super(Collection, self).save(*args, **kwargs)


class Collect(models.Model):
    '''
        relation between Collection and product is a manyTomany relationship
    '''
    shopify_id = models.BigIntegerField(
        primary_key=True, editable=False)
    collection = models.ForeignKey(
        'stores.Collection', on_delete=models.CASCADE,
        related_name='collect_product', editable=False)
    product = models.ForeignKey(
        'stores.Product', on_delete=models.CASCADE,
        related_name='collect_collection', editable=False)

    def save(self, *args, **kwargs):
        '''
            notice here we update the product gender if it's connected to
            some collection named with Man/Women
        '''
        collection = Collection.objects.get(
            shopify_id=self.collection_id)
        if (not collection.gender == 'N'):
            product = Product.objects.get(shopify_id=self.product_id)
            product.gender = collection.gender
            product.save()
        super(Collect, self).save(*args, **kwargs)


class RecurringCharge(models.Model):
    '''
        simple model to save the history of billing actions
    '''
    shopify_id = models.BigIntegerField(null=True)
    status = models.CharField(
        max_length=plan_status.max_length,
        choices=plan_status.choices,
        null=True)
    plan = models.CharField(
        max_length=plans.max_length,
        choices=plans.choices,
        null=True)
    store = models.ForeignKey(
        'stores.Store', on_delete=models.CASCADE,
        related_name='recurringCharges', editable=False)

    @staticmethod
    def billing_amount(plan):
        try:
            return cfg.PLANS[plan.split(" ")[0]][plan.split(" ")[1]]["Price"]
        except:
            raise ValidationError("not supported plan")
