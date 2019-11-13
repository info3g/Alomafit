from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from theming.models import Theme
from theming.serializers import ThemeSerializer


class ThemeViewSet(viewsets.ModelViewSet):
    """
    Authorized store owner only can add a new theme.
    """
    pagination_class = None
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication,)


def get_logo_image(request, image):
    img = open('/logos/' + image, 'r')
    return HttpResponse(img, content_type='img')
