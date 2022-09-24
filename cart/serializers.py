from rest_framework.serializers import  ModelSerializer, SerializerMethodField
from cart.models import Cart, CartItem
from product.serializers import ProductSerializer


class CartItemSerializer(ModelSerializer):
    product = ProductSerializer()
    total = SerializerMethodField()

    class Meta:
        model=CartItem
        fields= '__all__'

    def get_total(self, obj):
        return obj.total


class CartSerializer(ModelSerializer):
    items = CartItemSerializer(many=True)
    total = SerializerMethodField()

    class Meta:
        model=Cart
        fields= '__all__'

    def get_total(self, obj):
        return obj.total