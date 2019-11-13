import json

import requests

from stores.models import Store
from vfrlight.config import Config as cfg, Config

def webhooks_registration_problem():
    # although there are some webhooks that don't belong to products
    print('webhooks_registration_problem')
    pass

def get_webhooks(token, shop):
    headers = {
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json"
    }
    get_webhooks_response = requests.get("https://" + shop +
                                         "/admin/webhooks.json",
                                         headers=headers)
    if get_webhooks_response.status_code == 200:
        return json.loads(get_webhooks_response.text)
    else:
        return None

def alreadyRegistered(token, shop):
    webhooks = get_webhooks(token, shop)
    webhooks = [webhook['topic'] for webhook in webhooks['webhooks']]
    if len(webhooks) == 0:
        print("there is no webhook registered")
        return False
    if webhooks:
        result = webhooks.count(
            'products/update') == 1 and webhooks.count('products/create') == 1
        if result:
            return True
        else:
            webhooks_registration_problem()
            return False
    else:
        print('webhook request could not succeed')
        return False


def register_webhooks(token, shop, topic, Action):
    headers = {
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json"
    }

    # host must be something beside localhost
    payload = {
        "webhook": {
            "topic": topic,
            "address": "https://{0}/{1}".format(Config.HOST, Action),
            "format": "json"
        }
    }

    response = requests.post("https://" + shop
                                + "/admin/webhooks.json",
                                data=json.dumps(payload), headers=headers)
    if response.status_code == 201:
        print("{} has been registered".format(topic))

'''
    needs to be refactored, use shopify python api instead
'''


def _initilize_webhooks(store_slug):
    store = Store.objects.get(slug=store_slug)
    shop, token = store.url, store.token
    if alreadyRegistered(token, shop):
        print('webhooks registered')
        return
    reset_webhooks(token, shop)
    register_webhooks(
        token, shop, "products/update", "updateproduct")
    register_webhooks(
        token, shop, "products/create", "updateproduct")
    register_webhooks(
        token, shop, "products/delete", "deleteproduct")
    register_webhooks(
        token, shop, "app/uninstalled", "uninstalledapp")
    register_webhooks(
        token, shop, "collections/update", "updatecollection")
    register_webhooks(
        token, shop, "collections/delete", "updatecollection")
    register_webhooks(
        token, shop, "collections/create", "updatecollection")
    register_webhooks(
        token, shop, "shop/redact", "shop_redact")
    register_webhooks(
        token, shop, "customers/redact", "customers_redact")
    store.register_webhooks()


def reset_webhooks(token, shop):
    webhooks = get_webhooks(token, shop)['webhooks']
    webhooks_ids = [webhook['id'] for webhook in webhooks]
    if not len(webhooks_ids):
        print("there is no webhooks available to delete")
    for webhooks_id in webhooks_ids:
        reset_webhook(token, shop, webhooks_id)


def reset_webhook(token, shop, id):
    headers = {
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json"
    }
    get_webhooks_response = requests.delete("https://" + shop +
                                            "/admin/webhooks/{}.json".format(
                                                id),
                                            headers=headers)
    if get_webhooks_response.status_code == 200:
        print("webhook is deleted {}".format(id))
