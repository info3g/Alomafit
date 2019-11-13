from rest_framework import status, viewsets
from rest_framework.response import Response

from .serializers import *


class FitNonAuthenticatedViewSet(viewsets.ViewSet):
    '''
        fit product for non authenticated profiles,
        we need profile data as well as product id
    '''
    http_method_names = ['post', 'options']
    serializer_class = Fit_Product_Anonymous_Profile_Serializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            data = serializer.create(
                validated_data=serializer.data)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)


class FitAuthenticatedViewSet(viewsets.ViewSet):
    '''
        fit product for authenticated profiles
        we need profile_id and product_id
    '''
    http_method_names = ['post']
    serializer_class = Fit_Product_Authenticated_Profile_Serializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        profile_id = int(kwargs['id_pk'])
        if serializer.is_valid(raise_exception=ValueError):
            data = serializer.create(
                validated_data=serializer.data, profile_id=profile_id)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)


class PredictViewSet(viewsets.ViewSet):
    '''
        predict bust,hips,waist,shoulder from height,weight
        with it's coressponding metric cm/inch, kg/lb respectively
    '''
    http_method_names = ['post']
    serializer_class = PredictSerializer

    def create(self, request, *args):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            data = serializer.create(
                validated_data=serializer.data)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)
