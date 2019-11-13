import json
import traceback

from django.http import HttpResponse

from .models import Product, Store, Variant

def delete_product(request):
    """
        here we assume a webhook has been requested from shopify to
        delete some product, hence we verify the source via HMAC
    """
    product_data = json.loads(request.body)
    try:
        Product.objects.get(
            shopify_id=product_data['id']).delete()
    except Exception as e:
        print(e)
        traceback.format_exc()
        return HttpResponse(status=200)

    return HttpResponse(status=200)


def uninstalled_store(request):
    """
        Once an admin has uninstalled our app, we reset plan to be null.
        Shopify delete any registered webhooks/script_tags from its side so
        we have to do the same as well :)
    """
    try:
        store = Store.objects.get(url=request.webhook_domain)
        store.deactivate_any_plan()
        store.reset_webhooks()
        store.reset_scriptt_ags()
        store.products.all().delete()
    except Exception as e:
        print(e)
        traceback.format_exc()
        return HttpResponse(status=500)
    return HttpResponse(status=200)

def update_or_create_product_variant(request):
    """
        Here we assume the request has been verified that it's from shopify by the hmac
        we update the product data as well as its variants, hence in shopify the variants
        data get embedded in the product data
    """
    try:
        store = Store.objects.get(url=request.webhook_domain)
        product_db = update_or_create_product(
            request.webhook_data, store)
        update_or_create_variants(
            product_db, request.webhook_data["variants"])
    except:
        traceback.format_exc()
        return HttpResponse(status=200)
    return HttpResponse(status=200)


def update_or_create_product(p, store):
    """
        currently we fetch image url, title
    """
    image = p["images"][0]["src"] if (len(
        p["images"]) > 0) else "https://help.shopify.com/assets/shopify-full-color-black.svg"
    product_db = get_or_none(Product, shopify_id=p["id"])
    if product_db is None:
        product_db = Product.objects.create(
            shopify_id=p["id"], store=store, title=p["title"], image=image)
    else:
        product_db.title = p["title"]
        product_db.image = image
        # we are updating single instance; though, You need not user filter across table
        product_db.save()
    return product_db


def update_or_create_variants(product, variants):
    """
        Notice here variants data are embedded inside product data
        we fetch only title of the variant
    """
    for variant in variants:
        variant_db = get_or_none(Variant, shopify_id=variant['id'])
        if variant_db is None:
            variant_db = Variant.objects.create(shopify_id=variant['id'], product=product, title=variant['title'])
        else:
            variant_db.title = variant['title']
            variant_db.save()


def get_or_none(model, *args, **kwargs):
    """
        a utility method, return None just in case kwargs i.e some attributes
        shopify_id, title etc.... not found in model data
    """
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return None
