from django.http import Http404
from django.http import JsonResponse
from rest_framework import status, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from brands.models import Brand, ProductType, Size
from brands.serializers import BrandSerializer, ProductTypeSerializer, SizeSerializer, MeasurementsSerializer, \
    UnitSerializer

from django.core.mail import send_mail
from vfrlight.settings import EMAIL_HOST_USER
import sys
class BrandsAPIView(APIView):
    """
        View function return brands list.
    """

    def get(self, request, format=None):

        brands = Brand.objects.distinct('name')

        # Add Search based on the brand name.
        brand_name = request.query_params.get('brand', None)

        if brand_name:
            brands = brands.filter(name__icontains=brand_name).distinct('name')

        # Retrieve brands based on gender.
        gender = request.query_params.get('gender', None)
        if gender:
            brands = brands.filter(gender=gender).distinct('name')

        if brand_name and gender:
            brands = Brand.objects.all().filter(
                name__icontains=brand_name, gender=gender).distinct('name')

        serializer = BrandSerializer(brands, many=True)
        return Response(data=serializer.data)

    def post(self, request, format=None):
        send_mail(
            "Going to post brand",
            "Hello ",
            EMAIL_HOST_USER,
            ["surinder.indybytes@gmail.com"],
            fail_silently=True,
        )

        # This is for parse list object into string.
        if type(request.data['product_types']) == list:
            request.data['product_types'] = request.data['product_types'][0]['name']

        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class BrandDetailAPIView(APIView):
    """
        View function return brand using pk.
    """

    def get_object(self, pk):
        try:
            return Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        brand = self.get_object(pk)
        serializer = BrandSerializer(brand)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        brand = self.get_object(pk)
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        brand = self.get_object(pk)
        brand.delete()
        return Response(status=status.HTTP_200_OK)


class ProductTypeViewSet(ModelViewSet):
    queryset = ProductType.objects.distinct('name')
    serializer_class = ProductTypeSerializer
    # pagination_class = None
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('^name', '^gender')
    # permission_classes = (IsAuthenticatedOrReadOnly,)


class BrandsWithSlugViewSet(ModelViewSet):
    pagination_class = None
    serializer_class = BrandSerializer
    search_fields = ('^name', '^gender')
    filter_backends = (filters.SearchFilter,)
    parser_classes = (JSONParser, FormParser, MultiPartParser,)
    queryset = Brand.objects.filter(store_slug__isnull=False).exclude(
        store_slug__exact="").distinct('name')
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        slug = self.request.query_params.get('slug', None)
        if slug:
            self.queryset = self.queryset.filter(store_slug__icontains=slug)

        return self.queryset

    def perform_create(self, serializer):
        product_types = self.request.data.get('product_types')
        size_list = []
        for product_type in product_types:
            for size in product_type['sizes']:
                size_list.append(Size.objects.create(**size))
            product_type.pop('sizes')
            instance = ProductType.objects.create(**product_type)
            instance.sizes.set(size_list)
            size_list = []
        serializer.save()


@api_view(['GET', ])
@permission_classes((IsAuthenticatedOrReadOnly,))
def get_product_type_or_sizes(request):
    part = request.query_params.get('part', None)
    gender = request.query_params.get('gender', None)
    brand_name = request.query_params.get('brand', None)
    product_types = request.query_params.get('product_type', None)
    general_brands = Brand.objects.filter(name='general')

    if not brand_name and not product_types:
        return Response("brand or product_type field is required.")

    elif brand_name and gender and product_types and part:
        # Product Type -> Measurements
        brands = Brand.objects.filter(name__icontains=brand_name, product_types__icontains=product_types,
                                      gender=gender, part__icontains=part)#.distinct('part', 'measurements')
        if not brands:
            brands = general_brands.filter(product_types__icontains=product_types,
                                           gender=gender, part__icontains=part)#.distinct('part', 'measurements')
        serializer = MeasurementsSerializer(brands, many=True)
    elif brand_name and product_types and gender:
        # Brand and Product Type -> Sizes
        brands = Brand.objects.filter(name__icontains=brand_name, product_types=product_types, gender=gender)#.distinct(
            # 'sizes')
        if not brands:
            brands = general_brands.filter(product_types=product_types, gender=gender)#.distinct(
                # 'sizes')
        serializer = SizeSerializer(brands, many=True)

    elif brand_name and gender and not product_types:
        # Brand -> Product Type

        # products = Product.objects.distinct('title')
        # for product in products:
        #     if product.product_type in ['shirt', 't-shirt', 'blouse', 'top', 'tops']:
        #         part = 'tops'
        #         brands = Brand.objects.filter(part=part, name__icontains=brand_name).distinct('product_types')
        #         break
        #     else:
        #         brands = Brand.objects.filter(name__icontains=brand_name).distinct('product_types')
        #         break
        brands = Brand.objects.filter(
            name=brand_name, gender=gender)#.distinct('product_types')
        if not brands:
            brands = general_brands.filter(
                gender=gender)#.distinct('product_types')
        serializer = ProductTypeSerializer(brands, many=True)

    return JsonResponse(data=serializer.data, safe=False)


@api_view(['GET', ])
def get_brand_unit(request):
    brand = request.query_params.get('brand', None)
    product_types = request.query_params.get('product_type', None)
    gender = request.query_params.get('gender', None)
    if brand and product_types and gender:
        brandz = Brand.objects.filter(name=brand, product_types__icontains=product_types, gender=gender).distinct(
            'unit')
        if not brandz:
            brandz = Brand.objects.filter(name='general').distinct('name')
        brandz_serializer = UnitSerializer(brandz, many=True)
        return JsonResponse(data=brandz_serializer.data, safe=False)
    return JsonResponse(data="Brand not found.", safe=False)
