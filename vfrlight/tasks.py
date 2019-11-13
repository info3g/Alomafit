import requests
from django.core.mail import send_mail

from stores.models import Store
from vfrlight.celery import app
from vfrlight.config import Config as cfg
from vfrlight.initialization_util import _intitalize_scripttag
from vfrlight.settings import EMAIL_HOST_USER
from vfrlight.syncProducts_util import _sync_collections, _sync_products
from vfrlight.webhooks_util import _initilize_webhooks


def email(subject, text, to):
    send_mail(
        subject,
        text,
        EMAIL_HOST_USER,
        to,
        fail_silently=True,
    )


@app.task
def sync_products(store_slug):
    _sync_products(store_slug)


@app.task
def sync_collections(store_slug):
    _sync_collections(store_slug)


@app.task
def initilize_webhooks(store_slug):
    _initilize_webhooks(store_slug)


@app.task
def intitalize_scripttag(store_slug):
    _intitalize_scripttag(store_slug)


@app.task
def getlocaletaskandemail(store_slug):
    store = Store.objects.get(slug=store_slug)
    shop, token = store.url, store.token
    if store.primary_locale != "None":
        print("locale already fetched")
    else:
        headers = {
            "X-Shopify-Access-Token": token,
            "Content-Type": "application/json"
        }
        # host must be something beside localhost
        response = requests.get("https://" + shop
                                + "/admin/shop.json", headers=headers)
        try:
            j = response.json()
            store.set_primary_locale(j["shop"]["primary_locale"])
            print("slug : " + store.slug)
            print("Locale : " + store.primary_locale)
            print("locale from json" + j["shop"]["primary_locale"])
            shop_email = j["shop"]["email"]
            email(cfg.WELCOME_EMAIL_SUBJECT, cfg.WELCOME_EMAIL_CONTENT, [shop_email])
        except:
            print("error getting locale")
