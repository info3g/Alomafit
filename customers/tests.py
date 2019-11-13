from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from customers.generator import *
from customers.serializers import *
from vfrlight.util import fake_initialize
from vfrlight.util import generate_token


class RegisteringNewCustomerTestCase(TestCase):
    """Test suite for the api views."""

    def register_customer(self, authenticate=False):
        customer = CustomerFactory.build()
        response = self.client.post(
            reverse('rest_register'),
            {"username": customer.user.username,
             "password1": customer.user.password,
             "password2": customer.user.password,
             "email": customer.user.email},
            format="json")
        customer = Customer.objects.get(
            slug=slugify(customer.user.email))
        if authenticate:
            self.client.credentials(
                HTTP_AUTHORIZATION='JWT ' + generate_token(customer.user))
        return response, customer

    def register_customer_profile(self, authenticate=False,
                                  customer=None, profile=None):
        if not profile:
            profile = ProfileSerializer(ProfileFactory.build()).data
        if not customer:
            response, customer = self.register_customer(
                authenticate=authenticate)

        profile_serialized = ProfileSerializer(profile).data
        response = self.client.post(
            reverse('customers:customer-profiles-list',
                    kwargs={'slug_slug': slugify(customer.user.email)}),
            profile_serialized,
            format="json")
        profile = None
        if not response.status_code == status.HTTP_400_BAD_REQUEST:
            profile = Profile.objects.get(customer=customer)
        return response, customer, profile

    def add_to_closet(self, profile, product):
        response = self.client.post(
            reverse('customers:add_to_closet-list',
                    kwargs={'slug_slug': slugify(profile.customer.user.email),
                            'id_pk': profile.id}),
            {"product": product.shopify_id},
            format="json")
        added_to_closet = Product_Profile_Add_To_Closet.objects.get(
            customer_profile=profile, product=product)
        return response, added_to_closet

    @classmethod
    def setUpTestData(cls):
        """
            runs only one time, at the start
        """
        cfg.TESTING = True
        cfg.IGNORE_SYNC_DURING_CONNECT = False
        fake_initialize()

    def setUp(self):
        """
            runs before each TestCase
        """
        self.client = APIClient()

    # def test_api_predict(self):
    #     data = {
    #         'height': 174,
    #         'weight': 124,
    #         'metric_length': 'cm',
    #         'metric_weight': 'kg',
    #         'gender': 'M'
    #     }
    #
    #     response = self.client.post(
    #         reverse('fitalgorithms:predict-list'),
    #         data,
    #         format="json")
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #
    # def test_api_register__customer(self):
    #     self.register_customer()
    #     self.assertEqual(len(Customer.objects.all()), 1)
    #
    # def test_api_retrieve_customer(self):
    #     self.assertEqual(len(Customer.objects.all()), 0)
    #     response, customer = self.register_customer()
    #     self.client.credentials(
    #         HTTP_AUTHORIZATION='JWT ' + generate_token(customer.user))
    #     response = self.client.get(
    #         reverse('customers:customer-detail',
    #                 kwargs={'slug': slugify(customer.user.email)}),
    #         format="json")
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(
    #         response.data['slug'], slugify(customer.user.email))
    #
    def test_api_create_profile(self):
        self.assertEqual(len(Customer.objects.all()), 0)

        response, customer, profile = self.register_customer_profile()
        data = response.data
        self.assertAlmostEqual(data['height'], profile.height)
        self.assertAlmostEqual(data['weight'], profile.weight)
        self.assertAlmostEqual(data['bust'], profile.bust)
        self.assertAlmostEqual(data['waist'], profile.waist)
        self.assertAlmostEqual(data['shoulder'], profile.shoulder)
        self.assertEqual(data['gender'], profile.gender)
        self.assertEqual(data['metric_length'], profile.metric_length)

    # def test_api_create_duplicate_profiles(self):
    #     self.assertEqual(len(Customer.objects.all()), 0)
    #     response, customer, profile = self.register_customer_profile()
    #     response, customer, profile = self.register_customer_profile(customer=customer,
    #                                                                  profile=profile)
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #
    # def test_add_to_closet_get_non_authenticated(self):
    #     '''
    #         No authentication happened in here.
    #     '''
    #     response, customer, profile = self.register_customer_profile(
    #         authenticate=False)
    #     response = self.client.get(
    #         reverse('customers:add_to_closet-list',
    #                 kwargs={'slug_slug': slugify(customer.user.email),
    #                         'id_pk': profile.id}),
    #         format="json")
    #     self.assertEqual(response.status_code, 403)
    #
    # def test_add_to_closet_get_authenticated_different_profile(self):
    #     response, customer, profile = self.register_customer_profile(
    #         authenticate=True)
    #     # we are registering dummy customer
    #     response1, customer1, profile1 = self.register_customer_profile(
    #         authenticate=False)
    #     # Get request with the Non dummy customer
    #     response = self.client.get(
    #         reverse('customers:add_to_closet-list',
    #                 kwargs={'slug_slug': slugify(customer.user.email),
    #                         'id_pk': profile1.id}),
    #         format="json")
    #     self.assertEqual(response.status_code, 403)
    #
    # def test_add_to_closet_get_authenticated_different_user(self):
    #     response, customer, profile = self.register_customer_profile(
    #         authenticate=False)
    #     # we are registering dummy customer
    #     response1, customer1, profile1 = self.register_customer_profile(
    #         authenticate=False)
    #     # authenticate with the dummy customer
    #     self.client.credentials(
    #         HTTP_AUTHORIZATION='JWT ' + generate_token(customer1.user))
    #     # Get request with the Non dummy customer
    #     response = self.client.get(
    #         reverse('customers:add_to_closet-list',
    #                 kwargs={'slug_slug': slugify(customer.user.email),
    #                         'id_pk': profile.id}),
    #         format="json")
    #     # test will fail, i.e response will be 403
    #     self.assertEqual(response.status_code, 403)
    #
    # def test_add_to_closet_get(self):
    #     response, customer, profile = self.register_customer_profile(
    #         authenticate=True)
    #     response = self.client.get(
    #         reverse('customers:add_to_closet-list',
    #                 kwargs={'slug_slug': slugify(customer.user.email),
    #                         'id_pk': profile.id}),
    #         format="json")
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    # def test_add_to_closet_post(self):
    #     response, customer, profile = self.register_customer_profile(
    #         authenticate=True)
    #     # add to closet the first product
    #     data = {'product': Product.objects.all()[0].shopify_id}
    #     response = self.client.post(
    #         reverse('customers:add_to_closet-list',
    #                 kwargs={'slug_slug': slugify(customer.user.email),
    #                         'id_pk': profile.id}),
    #         data,
    #         format="json")
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #
    # def test_api_add_to_closet(self):
    #     response, customer, profile = self.register_customer_profile()
    #     product = Product.objects.all()[random.randint(
    #         0, Product.objects.count() - 1)]
    #     response, added_to_closet = self.add_to_closet(
    #         profile, product)
    #     self.assertEqual(added_to_closet.product, product)
    #     self.assertEqual(added_to_closet.customer_profile, profile)
    #
    # def test_populate_products(self):
    #     existed_products_count = Product.objects.count()
    #     populator = ProductPopulator()
    #     populator.populate(products_count=10, variants_count=2)
    #
    #     self.assertEqual(Product.objects.count(), 10 +
    #                      existed_products_count)
    #     self.assertGreaterEqual(Variant.objects.count(), 10)
    #
    # def test_populate_customers(self):
    #     populator = CustomerPopulator()
    #     populator.populate(customers_count=10, profiles_count=2)
    #
    #     self.assertEqual(Customer.objects.count(), 10)
    #     self.assertGreaterEqual(Profile.objects.count(), 10)
    #
    # def test_add_to_closet(self):
    #     ProductPopulator().populate(products_count=10, variants_count=2)
    #     CustomerPopulator().populate(customers_count=10, profiles_count=2)
    #     added_to_closet = 0
    #     for customer in Customer.objects.all():
    #         for profile in customer.customer_profile.all():
    #             product = Product.objects.all()[
    #                 random.randint(0, Product.objects.count() - 1)]
    #             Product_Profile_Add_To_Closet.objects.create(
    #                 customer_profile=profile, product=product)
    #             added_to_closet += 1
    #     self.assertEqual(added_to_closet,
    #                      Product_Profile_Add_To_Closet.objects.count())
    #
    # def test_most_added_to_closet(self):
    #     ProductPopulator().populate(products_count=30, variants_count=2)
    #     CustomerPopulator().populate(customers_count=10, profiles_count=2)
    #     most_added_to_closet_count = 0
    #     most_added_to_closet_product = Product.objects.all()[
    #         random.randint(0, Product.objects.count() - 1)]
    #     for customer in Customer.objects.all():
    #         for profile in customer.customer_profile.all():
    #             product = Product.objects.all()[
    #                 random.randint(0, Product.objects.count() - 1)]
    #             if(product == most_added_to_closet_product):
    #                 most_added_to_closet_count += 1
    #             Product_Profile_Add_To_Closet.objects.create(
    #                 customer_profile=profile, product=product)
    #             try:
    #                 with transaction.atomic():
    #                     Product_Profile_Add_To_Closet.objects.create(
    #                         customer_profile=profile,
    #                         product=most_added_to_closet_product)
    #                 most_added_to_closet_count += 1
    #             except:
    #                 # we don't allow the same profile to add the product twice to his closet
    #                 pass
    #     result = most_added_to_closet_product.store.most_added_to_closet[0]
    #     self.assertEqual(most_added_to_closet_product.shopify_id,
    #                      result['product_id'])
    #     self.assertEqual(most_added_to_closet_count,
    #                      result['count'])
    #
    # def test_try_product(self):
    #     ProductPopulator().populate(products_count=10, variants_count=6)
    #     CustomerPopulator().populate(customers_count=100, profiles_count=3)
    #     most_added_to_closet_count = 0
    #     most_added_to_closet_product = Product.objects.all()[
    #         random.randint(0, Product.objects.count() - 1)]
    #
    #     options = ['best_fit',
    #                'upper_size_best_fit_data',
    #                'lower_size_best_fit_data']
    #
    #     outputs = {option: {} for option in options}
    #     for customer in Customer.objects.all():
    #         for profile in customer.customer_profile.all():
    #             product = Product.objects.all()[
    #                 random.randint(0, Product.objects.count() - 1)]
    #             fit_product_output = fit_product(profile=profile,
    #                                              product=product)
    #         for variant in fit_product_output['results'].keys():
    #             for location in fit_product_output['results'][
    #                     variant]['stress_map'].keys():
    #                 if(not location in outputs[variant].keys()):
    #                     outputs[variant][location] = {}
    #                 if(not fit_product_output['results'][variant][
    #                         'stress_map'][location] in outputs[variant][location]):
    #                     outputs[variant][location][
    #                         fit_product_output['results'][variant]['stress_map']
    #                         [location]] = 0
    #                 outputs[variant][location][
    #                     fit_product_output['results'][variant]['stress_map']
    #                     [location]] += 1
    #     store_data = StoreSerializer(product.store).data
    #     # print (store_data)
    #     print(outputs)
    #     print()

    def test_fit_product_annonymous_profile(self):
        # just turn off any thing has to do with plan or ready_to_try

        cfg.DONT_CARE_ABOUT_PLAN = True
        cfg.DONT_CARE_ABOUT_READY_TO_TRY = True
        # just pick any random product
        p = Product.objects.all()[0]
        # create dummy profile
        profile_data = ProfileSerializer(ProfileFactory.build()).data
        data = {
            'product_id': p.shopify_id,
            'profile': profile_data
        }

        # fit product POST request
        response = self.client.post(
            reverse('fitalgorithms:fit_product-list'),
            data,
            format="json")
        # make sure it's created, i.e a new instance of `Profile_Try_Product` model
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # the same profile data, with the same product
        response = self.client.post(
            reverse('fitalgorithms:fit_product-list'),
            data,
            format="json")
        # Notice here, there is UNIQUE constraint on creating duplicate profiles
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # back to normal
        cfg.DONT_CARE_ABOUT_PLAN = False
        cfg.DONT_CARE_ABOUT_READY_TO_TRY = False

    # fit_product anonymous profile
    # fit_product registered profile
    # bodyshape insight in store
    # body size, bottom and top for male/ female insight on store
