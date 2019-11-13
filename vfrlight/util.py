from django.contrib.auth.models import User
from django.core.exceptions import (PermissionDenied)
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from stores.models import Merchant, Store
from vfrlight.config import Config as cfg
from vfrlight.tasks import (initilize_webhooks, intitalize_scripttag,
                            sync_collections, sync_products, getlocaletaskandemail)


def verify_store_access_token(request, store):
    jwt_token = request.META.get('HTTP_AUTHORIZATION')
    jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
    username = jwt_decode_handler(jwt_token.split(' ')[1])['username']
    if not store.owner.user.username == username:
        raise PermissionDenied()


def get_or_raise(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except Exception as e:
        raise serializers.ValidationError(e)


def generate_token(user):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    return token

from django.core.mail import send_mail
from vfrlight.settings import EMAIL_HOST_USER
import sys
def initialize(token, shop, ignore_webhooks=False, ignore_scripttag=False, source="connect"):
    try:
        user = User.objects.get(
            username=(shop + "_User"))
        merchant = Merchant.objects.get(user=user)
        store = Store.objects.get(owner=merchant)
        store.token = token
        store.save()
    except User.DoesNotExist:
        user = User.objects.create_user(
            username=shop + "_User", password='user12345')
        merchant = Merchant.objects.create(user=user)
        store = Store.objects.create(
            url=shop, token=token, owner=merchant)

    if ignore_webhooks:
        store.webhooks_added = True
        store.save()
    if ignore_scripttag:
        store.scripttag_added = True
        store.save()

    if cfg.getLocale:
        getLocale(store.slug)

    if cfg.Async:
        asynchronous_initialization(store.slug, source)
    else:
        non_asynchronous_initialization(store.slug, source)

    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(store.owner.user)
    token = jwt_encode_handler(payload)

    return store, token


def asynchronous_initialization(store_slug, source):
    # if source == "connect" and Store.objects.get(slug=store_slug).did_fetch_data_during_connect is True:
    #     return
    send_mail(
        "Welcome to asynchronous_initialization function",
        "Hello ",
        EMAIL_HOST_USER,
        ["surinder.indybytes@gmail.com"],
        fail_silently=True,
    )
    initilize_webhooks.delay(store_slug)
    intitalize_scripttag.delay(store_slug)
    # changed here not condition
    if cfg.IGNORE_SYNC_DURING_CONNECT:
        sync_products.delay(store_slug)
        sync_collections.delay(store_slug)
    if source == "connect":
        Store.objects.filter(slug=store_slug).update(did_fetch_data_during_connect=True)


def getLocale(store_slug):
    if cfg.IGNORE_SYNC_DURING_CONNECT:
        getlocaletaskandemail(store_slug)
    else:
        getlocaletaskandemail.delay(store_slug)


def non_asynchronous_initialization(store_slug, source):
    # if(not cfg.DEBUG):
    #     initilize_webhooks(store_slug)
    #     intitalize_scripttag(store_slug)
    if source == "connect" and Store.objects.get(slug=store_slug).did_fetch_data_during_connect is True:
        return
    initilize_webhooks(store_slug)
    intitalize_scripttag(store_slug)
    # for performance issues, do not sync when you are connecting
    if not cfg.IGNORE_SYNC_DURING_CONNECT:
        sync_products(store_slug)
        sync_collections(store_slug)
    if source == "connect":
        Store.objects.filter(slug=store_slug).update(did_fetch_data_during_connect=True)


def fake_initialize():
    initialize('1f145682dd384b589a7f1a2fa1bfc28f',
               'meet10.myshopify.com', ignore_webhooks=True,
               ignore_scripttag=True)
