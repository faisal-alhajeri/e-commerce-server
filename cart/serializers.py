from rest_framework.serializers import  ModelSerializer, SerializerMethodField
from cart.models import CartItem
from product.serializers import ProductSerializer


class CartItemSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model=CartItem
        fields= '__all__'
