from product.serializers import ProductSerializer
from .models import Order, OrderItem
from rest_framework.serializers import  ModelSerializer, SerializerMethodField

class OrderItemSerializer(ModelSerializer):
    total = SerializerMethodField()
    product = ProductSerializer()


    class Meta:
        model= OrderItem
        fields= '__all__'

    def get_total(self, obj):
        return obj.total

class OrderSerializer(ModelSerializer):
    items = OrderItemSerializer(many=True)
    total = SerializerMethodField()

    class Meta:
        model=Order
        fields= '__all__'

    def get_total(self, obj):
        return obj.total

    # def get_images(self, obj):
    #     return obj.get_images_urls()

