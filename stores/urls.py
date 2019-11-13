from django.conf.urls import include, url
from rest_framework_nested import routers

from insights.views import ProductTriedViewSet, VisitorViewSet
from stores.views import StoreViewSet, ActivatePlanViewSet, SyncViewSet, ProductViewSet, \
    NonAuthenticatedGetProductViewSet

app_name = 'stores'
router = routers.DefaultRouter()
router.register(r'stores', StoreViewSet)

stores_router = routers.NestedSimpleRouter(
    router, r'stores', lookup='store')

stores_router.register(
    r'visitors', VisitorViewSet, base_name='store-visitors')

stores_router.register(
    r'activate', ActivatePlanViewSet, base_name='store-activate-plan')

stores_router.register(
    r'sync', SyncViewSet, base_name='store-sync')

stores_router.register(
    r'products', ProductViewSet, base_name='store-products')

stores_router.register(
    r'nonauthenticatedgetproduct', NonAuthenticatedGetProductViewSet,
    base_name='nonauthenticated-get-product')

products_router = routers.NestedSimpleRouter(
    stores_router, r'products', lookup='product')
products_router.register(
    r'tries', ProductTriedViewSet, base_name='product_tries')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(stores_router.urls)),
    url(r'^', include(products_router.urls)),
]
