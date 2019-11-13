from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.schemas import get_schema_view
from rest_framework_jwt.views import (obtain_jwt_token, refresh_jwt_token,
                                      verify_jwt_token)
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

from vfrlight.views import *

schema_view = get_schema_view(title='Swagger API', renderer_classes=[
    OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [
    url(r'^docs/', schema_view, name="docs"),
    url(r'^auth-jwt/', obtain_jwt_token),
    url(r'^auth-jwt-refresh/', refresh_jwt_token),
    url(r'^auth-jwt-verify/', verify_jwt_token),
    url(r'^registration/', include('rest_auth.registration.urls')),
    url(r'^', include('rest_auth.urls')),
    url(r'^api/fittingroom/', include(('fitalgorithms.urls', 'fitalgorithms'),
                                      namespace='fitalgorithms')),
    url(r'^api/', include(('stores.urls', 'stores'),
                          namespace='stores')),
    url(r'^api/', include(('customers.urls', 'customers'),
                          namespace='customers')),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^connect$', connect),
    url(r'^install$', install),
    url(r'^updateproduct$', updateproduct),
    url(r'^deleteproduct$', deleteproduct),
    url(r'^uninstalledapp$', uninstalledapp),
    url(r'^updatecollection$', updatecollection),
    url(r'^shop/redact', shop_redact),
    url(r'^customers/redact', customers_redact),
    url(r'^checkbill$', checkbill),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^brands/', include('brands.urls')),
    url(r'^', include('apialgo.urls')),
    url(r'^', include('theming.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if (settings.DEBUG):
#     import debug_toolbar
#     urlpatterns = [
#         url(r'^__debug__/', include(debug_toolbar.urls))
#     ] + urlpatterns
