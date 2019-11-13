from django.core.exceptions import PermissionDenied
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from customers.permissions import *
from customers.serializers import *


class TriedProductsProfilePerspectiveViewSet(viewsets.ModelViewSet):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsCustomerProfiles, IsCustomerAuthenticated)
    http_method_names = ['get']
    serializer_class = TriedProductsProfilePerspectiveSerializer

    def get_queryset(self):

        profile_id = self.kwargs['id_pk']
        profile = get_or_raise(Profile, id=profile_id)
        # user = self.request.user._wrapped if hasattr(self.request.user, '_wrapped') else self.request.user
        # customer = get_or_raise(Customer, user=user)
        user = self.request.user._wrapped if hasattr(self.request.user, '_wrapped') else self.request.user
        if user.is_authenticated:
            customer = get_or_raise(Customer, user=user)
            if not profile.customer == customer:
                raise PermissionDenied
        else:
            raise PermissionDenied
        # TODO make distinct values
        queryset = Profile_Try_Product.objects.filter(profile=profile)

        return queryset

    class Meta:
        model = Profile_Try_Product
        fields = ('product', 'try_date')


class AddToClosetViewSet(viewsets.ModelViewSet):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsCustomerProfiles, IsCustomerAuthenticated)
    http_method_names = ['get', 'post']
    serializer_class = Product_Profile_Add_To_Closet_ProfilePerspectiveSerializer

    def create(self, request, *args, **kwargs):
        profile_id = self.kwargs['id_pk']
        serializer = self.serializer_class(data=request.data, context={
            'profile_id': profile_id})
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(
                validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        profile_id = self.kwargs['id_pk']
        profile = get_or_raise(Profile, id=profile_id)
        user = self.request.user._wrapped if hasattr(self.request.user, '_wrapped') else self.request.user
        if user.is_authenticated:
            customer = get_or_raise(Customer, user=user)
            if not profile.customer == customer:
                raise PermissionDenied
        else:
            raise PermissionDenied
        queryset = Product_Profile_Add_To_Closet.objects.filter(customer_profile=profile)
        queryset_data = []
        for obj in queryset:
            product_id = obj.__dict__['product_id']
            queryset_data.append({'product': product_id,
                                  'product_data': Product.objects.
                                 get(shopify_id=product_id)})
        return queryset_data

    class Meta:
        model = Product_Profile_Add_To_Closet
        fields = ('product',)


class ProfileViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsCustomerProfiles, IsCustomerAuthenticated)

    def update(self, request, *args, **kwargs):
        customer = get_or_raise(
            Customer, slug=self.kwargs['slug_slug'])
        serializer = self.serializer_class(data=request.data)
        '''
            we are pretty sure to get only one profile,
            but we pass Queryset for `update` only works like that
        '''
        profile_query_set = Profile.objects.filter(id=kwargs['pk'])
        if profile_query_set[0].customer == customer:
            if serializer.is_valid(raise_exception=ValueError):
                serializer.update(
                    validated_data=serializer.data, profile=profile_query_set)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        customer = get_or_raise(
            Customer, slug=self.kwargs['slug_slug'])
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            try:
                serializer.create(
                    validated_data=serializer.data, customer=customer)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                Response({"you are creating duplicate profile data for " +
                          "the same customer, watch out!"},
                         status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        customer = get_or_raise(
            Customer, slug=self.kwargs['slug_slug'])
        queryset = customer.customer_profile.all()
        return queryset


class CustomerViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    lookup_field = 'slug'
    queryset = Customer.objects.all()
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsCustomerAuthenticated,)
    serializer_class = CustomerSerializer

# class CustomObtainAuthToken(ObtainAuthToken):
#   def post(self, request, *args, **kwargs):
#      response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
#     token = Token.objects.get(key=response.data['token'])
#    return Response({'token': token.key, 'id': token.user_id})
