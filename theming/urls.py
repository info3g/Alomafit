from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers

from theming.views import ThemeViewSet

router = routers.DefaultRouter()
router.register(r'theming', ThemeViewSet)

urlpatterns = [
    url(r'', include(router.urls), name='theming'),
]

urlpatterns += staticfiles_urlpatterns()
