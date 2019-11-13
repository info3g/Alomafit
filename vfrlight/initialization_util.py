import json

import requests

from stores.models import Store


def initialize_shop(url):
    store, created = Store.objects.get_or_create(url=url)
    print("store created before {}".format(str(created)))
    return store


# note this could be a background job
# to synchronize our database for the first time with the store's products
# if it's not the first time then simple hit return


def initialize_products(store):
    pass


def _intitalize_scripttag(store_slug):
    store = Store.objects.get(slug=store_slug)
    shop, token = store.url, store.token
    link = "https://www.alomafit.com/sticky_try.js"
    # link = "http://indybytes.com/python/sticky_try.js"
    endpoint = "https://{}/admin/script_tags".format(shop)
    headers = {
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json"
    }
    payload = {
        "script_tag": {
            "event": "onload",
            "src": link
        }
    }
    response = requests.get(
        endpoint + ".json?src={}".format(link), headers=headers)
    data = json.loads(response.text)

    if len(data['script_tags']) == 0:
        for script_tag in data["script_tags"]:
            requests.delete(
                endpoint + "/{}.json".format(script_tag["id"]), headers=headers)
        response = requests.post(
            endpoint + ".json", json=payload, headers=headers)
        print("script _Tag {}".format(response.status_code))
    else:
        print('script_tag registered')
    store.register_script_tags()
    return response.status_code == 200
