from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from order.models import Order
from order.serializers import OrderSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_orders(request: HttpRequest):
    orders = Order.user_orders(request.user)
    s = OrderSerializer(orders, many=True)
    return Response(s.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def order(request: HttpRequest):
    profile = request.user.profile
    cart = profile.cart
    order = cart.order()
    s = OrderSerializer(order)
    return Response(s.data)
