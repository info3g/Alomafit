from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from brands.views import BrandsAPIView, BrandDetailAPIView, get_product_type_or_sizes, BrandsWithSlugViewSet, \
    get_brand_unit, ProductTypeViewSet

router = routers.DefaultRouter()
router.register(r'with-slug', BrandsWithSlugViewSet)
router.register(r'producttypes', ProductTypeViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^brands/', BrandsAPIView.as_view(), name="brands"),
    url(r'^(?P<pk>[0-9]+)/$', BrandDetailAPIView.as_view()),
    url(r'^product_type_or_size/', get_product_type_or_sizes, name='get_product_type_or_sizes'),
    url(r'^get_brand_unit/', get_brand_unit, name='get_brand_unit'),
]
