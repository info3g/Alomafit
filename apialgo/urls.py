from django.conf.urls import url, include
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers

from apialgo import views
from apialgo.views import MeasurementViewSet

router = routers.DefaultRouter()
router.register(r'measurements', MeasurementViewSet)

urlpatterns = [
    path('brasize/', views.brasize),
    path('getUnderBust', csrf_exempt(views.getUnderBust)),
    path('getFullBust', csrf_exempt(views.getFullBust)),
    path('GetBestFitTop', csrf_exempt(views.GetBestFitTop)),
    path('GetBestFitBottom', csrf_exempt(views.GetBestFitBottom)),
    path('GetBestFitDress', csrf_exempt(views.GetBestFitDress)),
    path('GetBestFit', csrf_exempt(views.GetBestFit)),
    path('GetMeasurements', csrf_exempt(views.GetMeasurements)),
    url(r'', include(router.urls), name='measurements'),
]
