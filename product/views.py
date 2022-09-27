from http.client import HTTPResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from product.models import Product, ProductCategory
from product.serializers import ProductCategorySerializer, ProductSerializer

# Create your views here.
@api_view(['GET'])
def all_products_view(request: HTTPResponse):
    products = Product.objects.all()
    s = ProductSerializer(products, many=True)
    return Response(s.data)

@api_view(['GET'])
def all_products_categories(request: HTTPResponse):
    categories = ProductCategory.objects.all()
    s = ProductCategorySerializer(categories, many=True)
    return Response(s.data)