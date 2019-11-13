import itertools
import time

import requests
import shopify

from fitalgorithms.get_mesaurements import get_meauserments
from stores.models import *


def get_or_none(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return None


def get_request(token, endpoint, shop):
    headers = {
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json"
    }
    response = requests.get(
        "https://{0}{1}".format(shop, endpoint), headers=headers)
    return response


def update_or_create_product_variant(p, store):
    product_db = update_or_create_product(p, store)
    update_or_create_variants(product_db, p["variants"])


def update_or_create_product(p, store):
    image = p["images"][0]["src"] if (len(
        p["images"]) > 0) else "https://help.shopify.com/assets/shopify-full-color-black.svg"
    product_db = get_or_none(Product, shopify_id=p["id"])
    if (product_db is None):
        product_db = Product.objects.create(
            shopify_id=p["id"], store=store, title=p["title"], image=image)
    else:
        product_db.title = p["title"]
        product_db.product_type = p["product_type"].lower() \
            if p['product_type'].lower() \
               in ProductTypeChoicesList \
            else ProductTypeChoicesList[0]
        product_db.image = image
        # we are updating single instance; though, You need not user filter across table
        product_db.save()
    return product_db


def update_or_create_variants(product, variants):
    for variant in variants:
        variant_db = get_or_none(Variant, shopify_id=variant['id'])
        if (variant_db is None):
            variant_db = Variant.objects.create(
                shopify_id=variant['id'], product=product, title=variant['title'])
        else:
            variant_db.title = variant['title']
            variant_db.save()

def _sync_products(store_slug):
    try:
        store = Store.objects.get(slug=store_slug)
        limit_pages = 250
        shopify.ShopifyResource.clear_session()
        with shopify.Session.temp(store.url, store.token):
            counts = shopify.Product.count()
            print(counts)

            # import pdb; pdb.set_trace()
            pages_count = counts // limit_pages + 1
            products_shopify = []
            for i in range(pages_count):
                products_shopify.append(shopify.Product.find(
                    limit=limit_pages, page=i,
                    fields="id,title,images,product_type," +
                           "vendor,updated_at,handle,created_at," +
                           "published_at,variants,collection_id"))

            products_shopify = list(
                itertools.chain.from_iterable(products_shopify))
            products_db = Product.objects.filter(store=store)
            products_shopify_id = [p.id for p in products_shopify]
            products_db_id = [p.shopify_id for p in products_db.all()]

            # those are not found our database and still found in shopify
            to_add_to_db = list(
                set(products_shopify_id).difference(set(products_db_id)))

            # those are not found shopify database but found in our database
            to_remove_from_db = list(
                set(products_db_id).difference(set(products_shopify_id)))

            to_not_update_from_db_trivially = to_remove_from_db + to_add_to_db

            # those might need to be updated
            to_update_into_db_UNFILTERED_YET = [
                product for product in products_db.all()
                if product.shopify_id not in to_not_update_from_db_trivially]

            products_shopify_dict = dict()
            for product_shopify in products_shopify:
                products_shopify_dict[product_shopify.id] = product_shopify

            products_db_dict = dict()
            for product_db in products_db:
                products_db_dict[product_db.shopify_id] = product_db

            # those need to be updated
            to_update_into_products_db = []
            for product_db in to_update_into_db_UNFILTERED_YET:
                '''
                    TODO implement update if product's data on shopify has changed
                    you may have to change django time zone
                '''
                product_shopify = products_shopify_dict[product_db.shopify_id]
                if (not Product.Shopify_objects.equal(product_shopify, product_db)):
                    to_update_into_products_db.append(product_db)

            # import pdb; pdb.set_trace()
            for product_id in to_remove_from_db:
                products_db_dict[product_id].delete()

            for product_id in to_add_to_db:
                product_to_add = products_shopify_dict[product_id]
                try:
                    Product.Shopify_objects.create_from_shopify(
                        store, product_to_add).save()
                except:
                    pass

            for product in to_update_into_products_db:
                # import pdb; pdb.set_trace()
                Product.Shopify_objects.update_from_shopify(
                    products_shopify_dict[product.shopify_id])
    except:
        pass

    for product in store.products.all():
        measure = get_meauserments("https://{}/products/{}".format(store.url, product.handle))
        print("Found measurements for {} : {}".format(product.handle, measure is not False))
        print("Product link : " + "https://{}/products/{}".format(store.url, product.handle))
        names_found = []
        if measure is not False:
            sizes_dict = {}
            sizes = measure.sizes
            for part in measure.parts:
                name = part.part.lower()
                if name == "hip":
                    name = "hips"
                if name == "shoulders":
                    name = "shoulder"
                names_found += [name]
                sizes_dict[name] = part.measurements
            i = 0
            print(sizes_dict)
            print(sizes)
            for size in sizes:
                try:
                    variant = product.variants.get(title__iexact=size)
                    if sizes_dict.get("hips", None) is not None:
                        variant.hips = sizes_dict["hips"][i]
                    if sizes_dict.get("shoulder", None) is not None:
                        variant.shoulder = sizes_dict["shoulder"][i]
                    if sizes_dict.get("bust", None) is not None:
                        variant.bust = sizes_dict["bust"][i]
                    if sizes_dict.get("waist", None) is not None:
                        variant.waist = sizes_dict["waist"][i]
                    variant.save()
                except Variant.DoesNotExist:
                    pass
                i += 1
            if len(names_found) > 0:
                product._required_attributes = names_found
                product.original_save()
        time.sleep(0.5)


def _sync_collections(store_slug):
    store = Store.objects.get(slug=store_slug)
    shopify.ShopifyResource.clear_session()
    with shopify.Session.temp(store.url, store.token):
        collections = shopify.CustomCollection.find()
        # build dictionary for shopify collections
        collections_shopify_dict = {collection.attributes['id']: collection
                                    for collection in collections}
        # filter our database against store collections based on ids
        collections_db = Collection.objects.filter(
            shopify_id__in=collections_shopify_dict.keys())
        collections_db_ids = []
        # iterate over store collection
        for collection in collections_db.all():
            collections_db_ids.append(collection.shopify_id)
            collection_shopify = collections_shopify_dict[collection.shopify_id]
            gender = Collection.gender_converter(collection_shopify.title)
            # if collection has been updated from shopify then update ours as well
            if (not (collection.gender == gender)):
                collection.title = collection_shopify.title
                collection.save()

        collections_ids_to_add_db = set(collections_shopify_dict.keys()).difference(
            set(collections_db_ids))

        for collection_id in collections_ids_to_add_db:
            collection_db = Collection.objects.create(
                shopify_id=collection_id,
                title=collections_shopify_dict[
                    collection_id].attributes['title'])

        # fetch from shopify all collects
        limit_pages = 250
        counts = shopify.Collect.count()
        pages_count = counts // limit_pages + 1
        collects_shopify = []
        for i in range(pages_count):
            collects_shopify.append(shopify.Collect.find(
                limit=limit_pages, page=i))
        # list them
        collects = list(
            itertools.chain.from_iterable(collects_shopify))
        # dictionarize them
        collects_shopify_dict = {
            collect.attributes['id']: collect for collect in collects}
        # filter our database for those collects
        collects_db = Collect.objects.filter(
            shopify_id__in=collects_shopify_dict.keys())
        # reference collects ids from our database
        collects_db_ids = [collect.shopify_id for collect in collects_db.all()]
        # check the collects that need to be added to our database
        collect_ids_to_add_db = set(collects_shopify_dict.keys()).difference(
            set(collects_db_ids))

        for collect_id in collect_ids_to_add_db:
            collect = collects_shopify_dict[collect_id]
            collect_db = Collect.objects.create(
                shopify_id=collect.attributes['id'],
                collection=Collection.objects.get(
                    shopify_id=collect.attributes['collection_id']),
                product=Product.objects.get(
                    shopify_id=collect.attributes['product_id']))
