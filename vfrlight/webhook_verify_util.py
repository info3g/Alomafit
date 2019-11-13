import base64
import hashlib
import hmac
import json

from django.conf import settings
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseForbidden)

from stores.model_webhook_util import (delete_product, uninstalled_store,
                                       update_or_create_product_variant)
from vfrlight.config import Config as cfg

def webhook_callback(request, value="update"):
    try:
        topic = request.META['HTTP_X_SHOPIFY_TOPIC']
        domain = request.META['HTTP_X_SHOPIFY_SHOP_DOMAIN']
        hmac = request.META['HTTP_X_SHOPIFY_HMAC_SHA256'] \
            if 'HTTP_X_SHOPIFY_HMAC_SHA256' in request.META else None
        data = json.loads(request.body.decode('utf-8'))
    except (KeyError, ValueError) as e:
        return HttpResponseBadRequest()

    if not domain_is_valid(domain):
        return HttpResponseBadRequest()

    # Verify the HMAC.
    if not hmac_is_valid(request.body, cfg.SHOPIFY_CONFIG['API_SECRET'], hmac):
        return HttpResponseForbidden()

    # Otherwise, set properties on the request object and return.
    request.webhook_topic = topic
    request.webhook_data = data
    request.webhook_domain = domain

    if value == "update" or value == "create":
        return update_or_create_product_variant(request)
    elif value == "delete":
        return delete_product(request)
    elif value == "uninstallapp":
        return uninstalled_store(request)
    return HttpResponse("NOT DEFINED", status=400)


def get_signal_name_for_topic(webhook_topic):
    """
    Convert a Shopify Webhook topic (eg "orders/create") to the equivalent Pythonic method name (eg "orders_create").
    """
    return webhook_topic.replace('/', '_')


def domain_is_valid(domain):
    """
    Check whether the given domain is a valid source for webhook request.
    """
    if domain is None:
        return False
    return len(domain) > 0


def get_hmac(body, secret):
    """
    Calculate the HMAC value of the given request body and secret as per Shopify's documentation for Webhook requests.
    See: http://docs.shopify.com/api/tutorials/using-webhooks#verify-webhook
    """
    hash = hmac.new(secret.encode('utf-8'), body, hashlib.sha256)
    return base64.b64encode(hash.digest()).decode()


def hmac_is_valid(body, secret, hmac_to_verify):
    """
    Return True if the given hmac_to_verify matches that calculated from the given body and secret.
    """
    return get_hmac(body, secret) == hmac_to_verify


def get_proxy_signature(query_dict, secret):
    """
    Calculate the signature of the given query dict as per Shopify's documentation for proxy requests.
    See: http://docs.shopify.com/api/tutorials/application-proxies#security
    """

    # Sort and combine query parameters into a single string.
    sorted_params = ''
    for key in sorted(query_dict.keys()):
        sorted_params += "{0}={1}".format(key,
                                          ",".join(query_dict.getlist(key)))

    signature = hmac.new(secret.encode(
        'utf-8'), sorted_params.encode('utf-8'), hashlib.sha256)
    return signature.hexdigest()


def proxy_signature_is_valid(request, secret):
    """
    Return true if the calculated signature matches that present in the query string of the given request.
    """

    # Allow skipping of validation with an explicit setting.
    # If setting not present, skip if in debug mode by default.
    skip_validation = getattr(
        settings, 'SKIP_APP_PROXY_VALIDATION', settings.DEBUG)
    if skip_validation:
        return True

    # Create a mutable version of the GET parameters.
    query_dict = request.GET.copy()

    # Extract the signature we're going to verify. If no signature's present, the request is invalid.
    try:
        signature_to_verify = query_dict.pop('signature')[0]
    except KeyError:
        return False

    calculated_signature = get_proxy_signature(query_dict, secret)

    # Try to use compare_digest() to reduce vulnerability to timing attacks.
    # If it's not available, just fall back to regular string comparison.
    try:
        return hmac.compare_digest(calculated_signature.encode('utf-8'), signature_to_verify.encode('utf-8'))
    except AttributeError:
        return calculated_signature == signature_to_verify
