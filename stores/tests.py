import time

from django.test import TestCase
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APIClient

from customers.generator import ProductPopulator
from vfrlight.syncProducts_util import _sync_collections, _sync_products
from vfrlight.util import fake_initialize, generate_token
from stores.generator import *
from stores.serializers import *


class init_TestCase(TestCase):
    """Test suite for the api views."""

    # def _products_on_init_not_ready(self):
    #     store = Store.objects.get(slug=slugify(self.shop))
    #     for product in store.products.all():
    #         self.assertFalse(product.ready_to_try

    def update_product_shopify(self, product_shopify, title=None,
                               product_type=None, vendor=None):
        # make a second copy for product's data that needs to be updated
        old_title = product_shopify.__dict__.get(
            'title', title)
        old_product_type = product_shopify.__dict__.get(
            'product_type', product_type)
        old_vendor = product_shopify.__dict__.get(
            'vendor', vendor)

        product_shopify.title = title if title else old_title
        product_shopify.product_type = product_type if product_type else old_product_type
        product_shopify.vendor = vendor if vendor else old_vendor
        success = product_shopify.save()
        self.assertTrue(success)

        return product_shopify, old_title, old_product_type, old_vendor

    def sync_with_shopify(self):
        try:
            startTime = time.time()
            _sync_products(self.store)
            t = time.time() - startTime
            print("products synced {0}: {1:0.3f}".format(self.id(), t))
            startTime = time.time()
            _sync_collections(self.store)
            t = time.time() - startTime
            print("collections synced {0}: {1:0.3f}".format(self.id(), t))
        except Exception as e:
            self.assertTrue(0, traceback.format_exc())

    def update_random_product(self):
        _range = Product.objects.count()
        product = Product.objects.all()[
            random.randint(0, _range - 1)]
        product_factory_serialized = update_product_factory(product)
        response = self.client.put(
            reverse('stores:store-products-detail',
                    kwargs={'store_slug': slugify(self.shop),
                            'pk': product.shopify_id}),
            product_factory_serialized,
            format="json")
        return response, product, product_factory_serialized

    def get_random_product_shopify(self):
        shopify.ShopifyResource.clear_session()
        with shopify.Session.temp(self.shop, self.token):
            # get random product from shopify
            product_shopify = shopify.Product.find()[
                random.randint(0, shopify.Product.count() - 1)]
            try:
                product_db = Product.objects.get(
                    shopify_id=product_shopify.id)
            except Exception as e:
                self.assertTrue(0, traceback.format_exc())

        return product_shopify, product_db

    def create_collect_shopify(self, product_id, collection_id):
        collect = shopify.Collect({'product_id': product_id,
                                   'collection_id': collection_id})
        success = collect.save()
        self.assertTrue(success)
        return collect

    def sync_create_product_shopify(self, collection="Women",
                                    title=Faker().words()[0],
                                    product_type=random.choice(
                                        ProductTypeChoicesList),
                                    vendor=Faker().company()):
        shopify.ShopifyResource.clear_session()
        with shopify.Session.temp(self.shop, self.token):
            collection = shopify.CustomCollection.find(
                title=collection)[0]
            new_product = shopify.Product()
            new_product, old_title, old_product_type, \
            old_vendor = self.update_product_shopify(new_product,
                                                     title=title,
                                                     product_type=product_type,
                                                     vendor=vendor)
            _ = self.create_collect_shopify(
                new_product.id, collection.attributes['id'])
            self.sync_with_shopify()

        return new_product.id, collection, title, product_type, vendor, new_product

    def sync_update_product_from_shopify(self,
                                         title=Faker().words()[0],
                                         product_type=random.choice(
                                             ProductTypeChoicesList),
                                         vendor=Faker().company()):
        shopify.ShopifyResource.clear_session()
        with shopify.Session.temp(self.shop, self.token):
            product_shopify, product_db = self.get_random_product_shopify()
            # update the product
            product_shopify, old_title, \
            old_product_type, old_vendor = self.update_product_shopify(
                product_shopify,
                title=title,
                product_type=product_type,
            )
            # since we deleted all collection that relate to the product as well as updated it's data
            self.sync_with_shopify()

        return product_shopify.id, old_title, old_product_type, old_vendor

    def ready_to_try_product_locally(self, ignore_variant=False):
        products_populated_ids = ProductPopulator(). \
            populate(products_count=10, variants_count=2,
                     ignore_variant=ignore_variant)
        products = Product.objects.filter(
            shopify_id__in=products_populated_ids)
        for product in products:
            self.assertEqual(product.ready_to_try,
                             ignore_variant == False)

    @classmethod
    def setUpTestData(self):
        '''
            runs only one time, at the start
        '''
        cfg.TESTING = True
        cfg.IGNORE_SYNC_DURING_CONNECT = False
        fake_initialize()

    def setUp(self):
        '''
            runs before each TestCase
        '''
        self.client = APIClient()
        self.store = Store.objects.all()[0]
        self.client.credentials(
            HTTP_AUTHORIZATION='JWT ' + generate_token(self.store.owner.user))
        self.shop, self.token = self.store.url, self.store.token
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print("{0}: {1:0.3f}".format(self.id(), t))

    def test_init(self):
        self.assertEqual(Store.objects.count(), 1)
        self.assertGreater(Product.objects.count(), 0)
        self.assertGreater(Variant.objects.count(), 0)
        self.assertGreater(Collection.objects.count(), 0)
        self.assertGreater(Collect.objects.count(), 0)
        self.assertEqual(Merchant.objects.count(), 1)

    def test_view_store(self):
        '''
            this test case uses JWT for authentication, note that all subsequent
            test cases will be prefixed with the same header,
            because we are saving it in self.client.credentials
        '''
        self.assertEqual(Store.objects.count(), 1)
        store = Store.objects.all()[0]
        response = self.client.get(
            reverse('stores:store-detail', kwargs={'slug': store.slug}),
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_put(self):
        response, product, product_factory = self.update_random_product()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def sync_create_product_shopify_collection_gender_test(self, collection="Women"):
        gender = Collection.gender_converter(collection)
        new_product_id, collection, title, \
        product_type, vendor, new_product = self.sync_create_product_shopify(
            collection=collection)
        product = Product.objects.get(shopify_id=new_product_id)
        self.assertEqual(product.gender, gender)
        self.assertEqual(product_type, product.product_type)
        shopify.ShopifyResource.clear_session()
        with shopify.Session.temp(self.shop, self.token):
            new_product.destroy()

    def test_product_sync_create_product(self):
        self.sync_create_product_shopify_collection_gender_test(
            collection="Women")
        self.sync_create_product_shopify_collection_gender_test(
            collection="Men")

    def test_product_sync_update_product_type_None_Value(self):
        '''
            if product_type is not a None value on our backend
            then if admin on shopify dashboard change it to some
            value that did not get recognized, then we will preserve the
            old value
        '''
        product_db = Product.objects.all()[0]
        old_product_type = product_db.product_type
        shopify.ShopifyResource.clear_session()
        with shopify.Session.temp(self.shop, self.token):
            product_shopify = shopify.Product.find(
                id=product_db.shopify_id)[0]
            self.update_product_shopify(product_shopify=product_shopify,
                                        title=product_db.title,
                                        vendor=product_db.vendor,
                                        product_type="None")
            self.sync_with_shopify()
            product_db = Product.objects.get(shopify_id=product_db.shopify_id)
            self.assertEqual(product_db.product_type, old_product_type)

    def test_product_sync_update_product_type_Not_None(self):
        '''
            if product_type is not a None value on our backend
            then if admin on shopify dashboard change it to some
            value that did not get recognized, then we will preserve the
            old value
        '''
        product_db = Product.objects.all()[0]
        old_product_type = product_db.product_type
        shopify.ShopifyResource.clear_session()
        with shopify.Session.temp(self.shop, self.token):
            product_shopify = shopify.Product.find(
                id=product_db.shopify_id)[0]
            self.update_product_shopify(product_shopify=product_shopify,
                                        title=product_db.title,
                                        vendor=product_db.vendor,
                                        product_type=ProductTypeChoicesList[2])
            self.sync_with_shopify()
            product_db = Product.objects.get(shopify_id=product_db.shopify_id)
            self.assertEqual(product_db.product_type,
                             ProductTypeChoicesList[2])

    def test_product_sync_delete_product(self):
        collection = "Women"
        gender = Collection.gender_converter(collection)
        new_product_id, collection, title, \
        product_type, vendor, new_product = self.sync_create_product_shopify(
            collection=collection)
        product = Product.objects.get(shopify_id=new_product_id)
        self.assertEqual(product.gender, gender)
        self.assertEqual(product_type, product.product_type)
        shopify.ShopifyResource.clear_session()
        with shopify.Session.temp(self.shop, self.token):
            new_product.destroy()
        try:
            product = Product.objects.get(shopify_id=new_product_id)
        except:
            product = None
        self.assertIsNotNone(product)
        self.sync_with_shopify()
        try:
            product = Product.objects.get(shopify_id=new_product_id)
        except:
            product = None
        self.assertIsNone(product)

    def test_product_ready_locally(self):
        self.ready_to_try_product_locally()

    def test_product_not_ready_locally(self):
        self.ready_to_try_product_locally(ignore_variant=True)
