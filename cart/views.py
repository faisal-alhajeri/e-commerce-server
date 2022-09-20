from django.http import HttpRequest
from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes


from cart.models import CartItem
from cart.serializers import CartItemSerializer
from product.models import Product

# Create your views here.


@api_view(['GET'])
# @parser_classes([JSONParser])
def get_all_cart_items(request: HttpRequest):
    items = CartItem.objects.filter(profile=request.user.profile)
    data = CartItemSerializer(items, many=True).data
    return Response(data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([JSONParser])
def add_to_cart(request: HttpRequest):
    product_uuid = request.data['product_uuid']
    quantity = request.data['quantity']
    product = Product.objects.get(pk=product_uuid)
    profile = request.user.profile

    old_cart_item: CartItem = CartItem.objects.filter(
        profile=profile, product=product).first()

    new_cart_item = None

    if old_cart_item:
        old_cart_item.quantity = quantity
        old_cart_item.save()  
        new_cart_item = old_cart_item
        if quantity == 0:
            old_cart_item.delete()

    elif quantity != 0:
        new_cart_item = CartItem.objects.create(
            profile=profile,
            product=product,
            quantity=quantity,
        )

    else:
        return Response({'detail': 'cant add to cart with 0 quantity'}, status=status.HTTP_400_BAD_REQUEST)

    s = CartItemSerializer(new_cart_item)
    return Response(s.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([JSONParser])
def delete_from_cart(request: HttpRequest):
    product_uuid = request.data['product_uuid']
    product = Product.objects.get(pk=product_uuid)
    profile = request.user.profile

    old_cart_item: CartItem = CartItem.objects.filter(
        profile=profile, product=product).first()

    if old_cart_item:
        old_cart_item.delete()

    return Response()



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([JSONParser])
def increment_cart(request: HttpRequest):
    product_uuid = request.data['product_uuid']
    product = Product.objects.get(pk=product_uuid)
    profile = request.user.profile


    new_cart_item = None
    old_cart_item: CartItem = CartItem.objects.filter(
        profile=profile, product=product).first()

    if old_cart_item:
        old_cart_item.quantity += 1
        old_cart_item.save()  
        new_cart_item = old_cart_item


    else:
        new_cart_item = CartItem.objects.create(
            profile=profile,
            product=product,
            quantity=1,
        )

    s = CartItemSerializer(new_cart_item)
    return Response(s.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([JSONParser])
def decrement_cart(request: HttpRequest):
    product_uuid = request.data['product_uuid']
    product = Product.objects.get(pk=product_uuid)
    profile = request.user.profile


    new_cart_item = None
    old_cart_item: CartItem = CartItem.objects.filter(
        profile=profile, product=product).first()

    if old_cart_item:
        old_cart_item.quantity -= 1
        old_cart_item.save()  
        new_cart_item = old_cart_item
        if old_cart_item.quantity == 0:
            old_cart_item.delete()


    s = CartItemSerializer(new_cart_item)
    return Response(s.data)