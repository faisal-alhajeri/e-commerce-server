from http.client import HTTPResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from product.forms import ProductCreateForm
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.decorators import parser_classes

from product.models import Product, ProductCategory, ProductImage
from product.serializers import ProductCategorySerializer, ProductSerializer

# Create your views here.
@api_view(['GET'])
def all_products_view(request: HTTPResponse):
    # get all products
    products = Product.objects.all()
    s = ProductSerializer(products, many=True)
    return Response(s.data)

@api_view(['GET'])
def single_products_view(request: HTTPResponse, product_uuid):
    # get a single product by uuid
    product = Product.objects.get(pk=product_uuid)
    s = ProductSerializer(product)
    return Response(s.data)


@api_view(['GET'])
def all_products_categories(request: HTTPResponse):
    # get all product categories
    categories = ProductCategory.objects.all()
    s = ProductCategorySerializer(categories, many=True)
    return Response(s.data)


# --------- admin views ----------------
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
@parser_classes([MultiPartParser])
def create_product(request: HTTPResponse):
    # admin can creaet new product
    data = request.POST
    form = ProductCreateForm(data)
    new_product: Product = form.save()
    new_product.add_images(request.FILES)
    return Response()

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
@parser_classes([MultiPartParser])
def update_product(request, product_uuid):
    # admin can update product
    old_product = Product.objects.get(pk=product_uuid)
    data = request.POST
    form = ProductCreateForm(data, instance=old_product)
    new_product: Product = form.save()
    new_product.add_images(request.FILES)
    return Response()

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_product(request: HTTPResponse, product_uuid):
    # admin can delete product
    old_product = Product.objects.get(pk=product_uuid)
    if old_product:
        old_product.delete()

    return Response()

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_product_image(request: HTTPResponse, image_uuid):
    # admin can delete product
    image = ProductImage.objects.get(pk=image_uuid)
    # print(image)
    if image:
        image.delete()
    return Response()

