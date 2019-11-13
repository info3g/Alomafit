class Config:
    SECRET_KEY = "CantStopAddictedToTheShinDigChopTopHeSaysImGonnaWinBig"
    # HOST = "obscure-caverns-78108.herokuapp.com"
    HOST = "alomafit.herokuapp.com"
    # HOST = "c2597ed0.ngrok.io"

    DEBUG = True
    TESTING = False
    '''
        It's quite important for tasks independent from front-end such as
        Script_tag and Webhooks registration when app is being installed for
        the first time ...
    '''
    Async = True
    # Before shopify sets a new recurring charge monthly, we leave 6 months for free and 5000 tries
    FREE_TRIAL = 364 / 2

    BILLING_CYCLE_IN_DAYS = 30

    PLANS = {
        'Male': {
            'Free': {
                'Tries': 500,
                'Price': 0,
                'Time': FREE_TRIAL
            },
            'First': {
                'Tries': 10000,
                'Price': 45,
                'Time': BILLING_CYCLE_IN_DAYS
            },
            'Second': {
                'Tries': 15000,
                'Price': 75,
                'Time': BILLING_CYCLE_IN_DAYS
            },
            'Customized': {
                'Tries': 1000000000,
                'Price': 175,
                'Time': BILLING_CYCLE_IN_DAYS
            }
        },
        'Female': {
            'Free': {
                'Tries': 500,
                'Price': 0,
                'Time': FREE_TRIAL
            },
            'First': {
                'Tries': 7000,
                'Price': 45,
                'Time': BILLING_CYCLE_IN_DAYS
            },
            'Second': {
                'Tries': 15000,
                'Price': 75,
                'Time': BILLING_CYCLE_IN_DAYS
            },
            'Customized': {
                'Tries': 1000000000,
                'Price': 175,
                'Time': BILLING_CYCLE_IN_DAYS
            }
        },
        'MaleAndFemale': {
            'Free': {
                'Tries': 500,
                'Price': 0,
                'Time': FREE_TRIAL
            },
            'First': {
                'Tries': 7000,
                'Price': 75,
                'Time': BILLING_CYCLE_IN_DAYS
            },
            'Second': {
                'Tries': 15000,
                'Price': 95,
                'Time': BILLING_CYCLE_IN_DAYS
            },
            'Customized': {
                'Tries': 1000000000,
                'Price': 195,
                'Time': BILLING_CYCLE_IN_DAYS
            }
        }
    }

    FRONT_END_HOST = "https://alomafit.herokuapp.com/"
    SHOPIFY_CONFIG = {
        'API_KEY': '30e5f7a76d8bbe744ad2a73944ac48f7',
        'API_SECRET': '4266e4dfba32df7931e0ad76494f9b3e',
        'APP_HOME': 'https://' + HOST,
        'CALLBACK_URL': 'https://' + HOST + '/install',
        'CHARGES_RETURN_URL': 'https://' + 'alomafit.com/newApp/new-dash/charge.html?charge_id',
        # 'REDIRECT_URI': 'https://' + HOST + '/connect',
        'REDIRECT_URI': 'https://' + 'alomafit.com/newApp/new-dash/auth.html',
        'SCOPE': ['read_products', 'write_script_tags', 'read_product_listings']
    }

    EXPERIMENT = {
        'customers_count': 100, 'profiles_count': 3,
        'products_count': 25, 'variants_count': 6,
        'added_to_closet_propability': 0.6
    }
    if DEBUG and TESTING:
        SHOPIFY_CONFIG['SCOPE'].append('write_products')
        SHOPIFY_CONFIG['SCOPE'].append('write_product_listings')
    # those babies should not pay for any charge
    DEVELOPMENT_STORES = ['alomafit-vfr-light-demo.myshopify.com',
                          'profit-demo-store.myshopify.com',
                          'islam-mesha.myshopify.com',
                          'jbrtest.myshopify.com', 'meet10.myshopify.com',
                          'mohammadstore-2.myshopify.com',
                          'muhammads-test-store.myshopify.com',
                          'osamahstore.myshopify.com',
                          'faditest123.myshopify.com',
                          'jaber-testing.myshopify.com',
                          'your-fashion-store-name.myshopify.com',
                          'facebookpixel-test.myshopify.com',
                          'profitapptesting.myshopify.com']
    # just in case, we want to test some code without paying attention to those constraints
    DONT_CARE_ABOUT_PLAN = False
    DONT_CARE_ABOUT_READY_TO_TRY = False
    # just do not sync the store data, in the connect process
    IGNORE_SYNC_DURING_CONNECT = True

    # fetch Products data Every Time user connects
    SYNC_PRODUCTS_EVERY_TIME_A_USER_CONNECT = True

    # re fetch products data when user hits synchronize

    REFRESH_PRODUCTS_EVERY_TIME_USER_SYNC = True

    # Get Locale Language
    getLocale = True

    # Email settings first time
    WELCOME_EMAIL_SUBJECT = "Thanks for installing ProFit App"
    WELCOME_EMAIL_CONTENT = "Hi,\nThank you for installing ProFit App. \n\nPlease take a look at our how " \
                            "to guide for this App at: https://www.alomafit.com/how-to-guide/ .\n\n\n\nShould you " \
                            "have any question please check our FAQ at https://www.alomafit.com/how-to-guide/faq/ . " \
                            "You can always reach us at support@alomafit.com for any issue, suggestion or " \
                            "request.\n\n\n\nBest regards,\n\n\n\nProFit Customers Support Team "
