from django.conf.urls import include, url
from rest_framework_nested import routers

from insights.views import HitProductViewSet, StillInFittingRoom_ViewSet
from .views import *

app_name = 'fitalgorithms'

predict_router = routers.DefaultRouter()
'''
    here predict process is profile ignostic, we just need height and weight
    with its coressponding metrics cm/inch , kg/lb respectively
'''
predict_router.register(
    r'predict', PredictViewSet, base_name='predict')

fit_product_router = routers.DefaultRouter()
'''
    here we have different api for authenticated and non authenticated profiles
    we need profile data such as height,weight,bust,hips,etc... and the product_id
'''
fit_product_router.register(
    r'fit_product', FitNonAuthenticatedViewSet, base_name='fit_product')

hit_product_router = routers.DefaultRouter()
# its solely used for insightsm we record time spent on fitting room
hit_product_router.register(
    r'hit_product', HitProductViewSet, base_name='hit_product')
stillInFittingRoom_router = routers.DefaultRouter()
'''
    Every time interval that front-end and backend agreed upon this will be called
    to update time spent on fitting room by specific profile hence we don't need
    to know what the profile is, we are using token based authentication with this api
    because these info is required for authenticated and non authenticated profiles
'''
stillInFittingRoom_router.register(
    r'still', StillInFittingRoom_ViewSet, base_name='still'
)

urlpatterns = [
    url(r'^', include(predict_router.urls)),
    url(r'^', include(fit_product_router.urls)),
    url(r'^', include(hit_product_router.urls)),
    url(r'^', include(stillInFittingRoom_router.urls)),
]
