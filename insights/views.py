from rest_framework import status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from fitalgorithms.serializers import *
from insights.serializers import TriedProductsFromProductPerspectiveViewSet, Store_Visitor_Serializers, \
    HitProduct_Serializer, StillInFittingRoom_Serializer
from stores.models import Store


class StandardResultsSetPagination(PageNumberPagination):
    # here we are setting custom pagination
    page_size = 40
    page_size_query_param = 'page_size'
    max_page_size = 1000


class VisitorViewSet(viewsets.ModelViewSet):
    """
        list all profiles that tried some product to some store
        hence we know from product the store that got visited
    """
    # authentication_classes = (
    #     JSONWebTokenAuthentication, SessionAuthentication, BasicAuthentication)
    http_method_names = ['get']
    serializer_class = Store_Visitor_Serializers
    # since profiles may grow very large, we need to specify large page size
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        store = get_or_raise(Store, slug=self.kwargs['store_slug'])
        queryset = Profile_Visit_Store.objects.filter(store=store)
        return queryset


class ProductTriedViewSet(viewsets.ModelViewSet):
    """
        list all profiles that tried some product with the coressponding tried date
    """
    # authentication_classes = (
    #     JSONWebTokenAuthentication, SessionAuthentication, BasicAuthentication)
    http_method_names = ['get']
    serializer_class = TriedProductsFromProductPerspectiveViewSet

    def get_queryset(self):
        product = Product.objects.get(
            shopify_id=self.kwargs['product_pk'])
        queryset = Profile_Try_Product.objects.filter(product=product)
        return queryset


class HitProductViewSet(viewsets.ViewSet):
    """
        Here we assume that when authenticated/non authenticated profile started the
        fitting room, a new HitProduct instance will be created to keep track
        of time spent on it, it returns a token to further more update the time spent
        on it,  @see StillInFittingRoom_ViewSet
    """
    http_method_names = ['post']
    serializer_class = HitProduct_Serializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            data = serializer.create(
                validated_data=serializer.data)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)


class StillInFittingRoom_ViewSet(viewsets.ViewSet):
    """
        To update the time spent on the fitting room by some authenticated/non authenticated
        profile, first we assume there is a HitProduct instance was created previously
        and a valid token is presented here to get the HitProduct instance.
        Hence Profile could hit any product's fitting room as well as the same product's
        fitting room could be hit by many profiles
    """
    http_method_names = ['post']
    serializer_class = StillInFittingRoom_Serializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            data = serializer.create(
                validated_data=serializer.data)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)
