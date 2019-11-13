import json

import requests

from vfrlight.settings import ALLOWED_HOSTS


def AddRecurringCharge(shop, token, price, trial_period=30, test=None, name="AlomaFitCharge"):
    headers = {
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json"
    }
    payload = {
        "recurring_application_charge": {
            "name": name,
            "test": test,
            "price": price,
            "trial_days": trial_period,
            "return_url": "https://" + ALLOWED_HOSTS[0] + "/checkbill"
        }
    }
    response = requests.post("https://" + shop + "/admin/recurring_application_charges.json", headers=headers
                             , data=json.dumps(payload))
    return json.loads(response.text).get("recurring_application_charge")


def GetChargeById(shop, token, charge_id):
    headers = {
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json"
    }
    response = requests.get("https://" + shop + "/admin/recurring_application_charges/{}.json".format(charge_id)
                            , headers=headers)
    return json.loads(response.text).get("recurring_application_charge")


def ActivateChargeById(shop, token, charge_id):
    headers = {
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json"
    }
    response = requests.post(
        "https://" + shop + "/admin/recurring_application_charges/{}/activate.json".format(charge_id),
        headers=headers)
    return json.loads(response.text).get("recurring_application_charge")
