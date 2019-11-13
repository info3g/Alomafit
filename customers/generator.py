import factory.fuzzy
from django.db import transaction

from customers.models import *
from fitalgorithms.algorithms import fit_product
from stores.generator import *
from stores.models import *


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    user = factory.SubFactory(
        'customers.generator.UserFactory')


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    name = factory.Faker('first_name')
    gender = factory.fuzzy.FuzzyChoice(['M', 'F'])
    # TODO since fitalgorithms doesn't offer function to convert from cm to inch
    metric_length = 'cm'
    # TODO since fitalgorithms doesn't offer function to convert from lb to kg
    metric_weight = 'kg'
    skin = factory.fuzzy.FuzzyChoice(['dark', 'light'])

    @factory.lazy_attribute
    def height(self):
        (min_value, max_value) = (min_height_cm_male, max_height_cm_male) \
            if self.gender == "M" else (min_height_cm_female, max_height_cm_female)
        height = factory.fuzzy.FuzzyFloat(min_value, max_value)
        return height.fuzz()

    @factory.lazy_attribute
    def weight(self):
        (min_value, max_value) = (min_weight_kg_male, max_weight_kg_male) \
            if self.gender == "M" else (min_weight_kg_female, max_weight_kg_female)
        weight = factory.fuzzy.FuzzyFloat(min_value, max_value)
        return weight.fuzz()

    @factory.lazy_attribute
    def bust(self):
        bust = factory.fuzzy.FuzzyFloat(
            VariantRangesDict.profile_ranges['bust'][self.gender][0],
            VariantRangesDict.profile_ranges['bust'][self.gender][1])
        return bust.fuzz()

    @factory.lazy_attribute
    def waist(self):
        waist = factory.fuzzy.FuzzyFloat(
            VariantRangesDict.profile_ranges['waist'][self.gender][0],
            VariantRangesDict.profile_ranges['waist'][self.gender][1])
        return waist.fuzz()

    @factory.lazy_attribute
    def hips(self):
        hips = factory.fuzzy.FuzzyFloat(
            VariantRangesDict.profile_ranges['hips'][self.gender][0],
            VariantRangesDict.profile_ranges['hips'][self.gender][1])
        return hips.fuzz()

    @factory.lazy_attribute
    def shoulder(self):
        shoulder = factory.fuzzy.FuzzyFloat(
            VariantRangesDict.profile_ranges['shoulder'][self.gender][0],
            VariantRangesDict.profile_ranges['shoulder'][self.gender][1])
        return shoulder.fuzz()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "person{}".format(n + 1))
    password = 'person12345'
    email = factory.Sequence(
        lambda n: 'person{0}@example.com'.format(n))


class ProductPopulator:
    """
        Since faker could bring the same name twice,
        We need to make sure stores are unique by their url
    """

    @staticmethod
    def create_store(owner):
        global store
        created_store = False
        while not created_store:
            try:
                store = Store.objects.create(owner=owner, url='{}.myshopify.com'.format(factory.Faker('first_name')),
                                             token='12345')
                created_store = True
            except MemoryError:
                print('Some Exception')
        return store

    def populate(self, store=None, products_count=10, variants_count=2, ignore_variant=False):
        """
            populate our database with fake products data
        """
        if not store:
            # first of all we create a user
            user = UserFactory.create()
            # a merchant instance is also created, with a OneToOne relation with the user
            merchant = Merchant.objects.create(user=user)
            # creating fake store requires a merchant instance,
            store = self.create_store(merchant)
        products_populated_ids = []
        for i in range(products_count):
            products_populated_ids.append(i)
            # create on the fly a product data
            product_shopify_id = Product.objects.count()
            product = Product.objects.create(shopify_id=product_shopify_id,
                                             store=store,
                                             title="p {}".format(i))
            for j in range(random.randint(1, variants_count)):
                # generate its variants, since variant has a foreign key to product
                Variant.objects.create(title="{} v {}".format(product.title, j), shopify_id=Variant.objects.count(),
                                       product=product)
            """
                here we update the product data such as fabric,stretch,
                elasticity,product type, hence ignore_variant is used to indicate
                whether we want to update its variants data as well,
                return a serializer object
            """
            product_serialized = updateProduct_factory(
                product, ignore_variant=ignore_variant)
            for variant in product_serialized['variants']:
                Variant.objects.filter(shopify_id=variant[
                    'shopify_id']).update(**variant)
            """
                We delete from the returned serializer those fields which are not
                needed during the update routine of the product in our database
            """
            del product_serialized['variants']
            """
                 for clarification, such fields like those are property
                 which are dynamically generated
            """
            del product_serialized['ready_to_try']
            del product_serialized['covered_by_the_plan']
            """
                update method only work in bulk mode,
                i.e it needs a queryset to get it work instead of a single instance
            """
            Product.objects.filter(shopify_id=product_shopify_id).update(
                **product_serialized)
        return products_populated_ids


class CustomerPopulator:

    def populate(self, customers_count=10, profiles_count=2):

        for i in range(customers_count):
            customer = CustomerFactory.create()
            for j in range(random.randint(1, profiles_count)):
                try:
                    '''
                        make sure that we don't create two profiles
                        with the same name and customer instance
                    '''
                    profile = ProfileFactory.create()
                    with transaction.atomic():
                        customer.customer_profile.add(profile)
                except MemoryError:
                    '''
                        with random name generator, if name of profile occurred
                        twice, this violates unique constraint.
                     '''
                    j - 1


class Experiment:

    @staticmethod
    def test1(customers_count=100, profiles_count=3, products_count=10, variants_count=6,
              added_to_closet_propability=0.6, store=None):
        ProductPopulator().populate(products_count=products_count,
                                    variants_count=variants_count,
                                    store=store)
        # CustomerPopulator().populate(customers_count=customers_count,
        #                              profiles_count=profiles_count)
        most_added_to_closet_count = 0
        most_added_to_closet_product = Product.objects.all()[
            random.randint(0, Product.objects.count() - 1)]

        for customer in Customer.objects.all():
            for profile in customer.customer_profile.all():
                product = Product.objects.all()[
                    random.randint(0, Product.objects.count() - 1)]
                fit_product(profile=profile, product=product)
                if random.uniform(0, 1) > added_to_closet_propability:
                    product.yet_added_to_his_closet(profile)
