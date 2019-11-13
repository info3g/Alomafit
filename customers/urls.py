from django.conf.urls import include, url
from rest_framework_nested import routers

from customers.views import *
from fitalgorithms.views import FitAuthenticatedViewSet

app_name = 'customers'
router = routers.SimpleRouter()
router.register(r'customers', CustomerViewSet)
# CRUD api on customer are defined by the slug of its user email address
customers_router = routers.NestedSimpleRouter(
    router, r'customers', lookup='slug')
# here we are nesting profile to lie under customer slug
customers_router.register(
    r'profiles', ProfileViewSet, base_name='customer-profiles')
# CRUD api on profile, we are identifying each profile with its id
profiles_router = routers.NestedSimpleRouter(
    customers_router, r'profiles', lookup='id')
'''
    when the profile is authenticated i.e there is customer instance related to it
    we only need the product id and the profile id, to run fit algorithms.
'''
profiles_router.register(
    r'fit_product', FitAuthenticatedViewSet, base_name='fit_product')
# profile has the option to add products to his closet
profiles_router.register(
    r'add_to_closet', AddToClosetViewSet, base_name='add_to_closet')
# we could list all the products that are tried by specific profile with its corresponding date
profiles_router.register(
    r'tried_products', TriedProductsProfilePerspectiveViewSet, base_name='tried_products')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(customers_router.urls)),
    url(r'^', include(profiles_router.urls)),
    # url(r'^authenticate/', CustomObtainAuthToken.as_view()),
]
