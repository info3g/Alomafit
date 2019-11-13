import json
from uuid import uuid4

import shopify
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from rest_framework.response import Response

from stores.models import RecurringCharge
from vfrlight.config import Config as cfg
from vfrlight.util import initialize
from vfrlight.webhook_verify_util import webhook_callback


from django.core.mail import send_mail
from vfrlight.settings import EMAIL_HOST_USER
import sys
@require_http_methods(["GET"])
def install(request):
    if "shop" in request.GET:
        shop = request.GET["shop"]
    else:
        return HttpResponse("Error:parameter shop not found", status=500)
    # generate random sense to authenticate origin after redirect
    state = str(uuid4())
    shopify.ShopifyResource.clear_session()
    request.session['state'] = state
    shopify.Session.setup(
        api_key=cfg.SHOPIFY_CONFIG["API_KEY"], secret=cfg.SHOPIFY_CONFIG["API_SECRET"])
    permission_url = shopify.Session(shop.strip()).create_permission_url(
        cfg.SHOPIFY_CONFIG["SCOPE"], cfg.SHOPIFY_CONFIG["REDIRECT_URI"])
    permission_url = permission_url + "&state={}".format(state)
    return HttpResponseRedirect(permission_url)


# @require_http_methods(["GET"])
# def connect(request):
#     logging.debug("Connect Function")
#     # HEROKU bug
#     # if(not(request.session.get('state') == request.GET.get('state'))):
#     #     return HttpResponse("Request origin cannot be verified")
#     try:
#         # authentication & integrity is done via the request_token
#         token = shopify.Session(
#             request.GET['shop']).request_token(params=request.GET)
#     except Exception as e:
#         return HttpResponse(e)
#
#     store = initialize(token, request.GET['shop'])
#     return HttpResponse('Hi There')
#


@require_http_methods(["POST"])
def connect(request):
    data = {}
    try:
        data = json.loads(str(dict(request.POST))[2:-8])
        shopify.Session.setup(
            api_key=cfg.SHOPIFY_CONFIG["API_KEY"],
            secret=cfg.SHOPIFY_CONFIG["API_SECRET"])

        data['token'] = shopify.Session("%s" % (
            data['shop'])).request_token(params=data)

        store, token = initialize(
            token=data['token'], shop=data['shop'])

        data = {'token': token}

    except Exception:
        print('Exception happened.')

    return HttpResponse(json.dumps(data))


@require_http_methods(["POST"])
def updateproduct(request):
    return webhook_callback(request)


@require_http_methods(["POST"])
def uninstalledapp(request):
    send_mail(
        "Welcome to uninstalledapp function : ",
        "Hello " + str(request.POST),
        EMAIL_HOST_USER,
        ["surinder.indybytes@gmail.com"],
        fail_silently=True,
    )
    return webhook_callback(request, value="uninstallapp")


@require_http_methods(["POST"])
def deleteproduct(request):
    return webhook_callback(request=request, value="delete")


@require_http_methods(["POST"])
def updatecollection(request):
    """
        Make it a background process to re sync collections
        Or refactor webhooks into seperated app, and make an optimized sync
    """
    # return _sync_collections
    return HttpResponse(status=200)


@require_http_methods(["POST"])
def shop_redact(request):
    """
        GDPR requirements
    """
    return HttpResponse(status=200)


@require_http_methods(["POST"])
def customers_redact(request):
    """
        GDPR requirements
    """
    return HttpResponse(status=200)


@api_view(['GET'])
def checkbill(request):
    charge_id = request.GET['charge_id']
    charge_db = RecurringCharge.objects.get(shopify_id=charge_id)
    store = charge_db.store
    shopify.ShopifyResource.clear_session()
    with shopify.Session.temp(store.url, store.token):
        charge = shopify.RecurringApplicationCharge.find(charge_id)
        if charge.attributes['status'] == 'accepted':
            charge.activate()
            store.activate_plan(charge.attributes['name'])
        charge_db.status = charge.attributes['status']
        charge_db.save()
    return Response({'data': {'plan': charge_db.plan,
                              'status': charge_db.status}}, status=200)
