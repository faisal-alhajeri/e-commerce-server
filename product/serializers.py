from .models import Product
from rest_framework.serializers import  ModelSerializer, SerializerMethodField

class ProductSerializer(ModelSerializer):
    images = SerializerMethodField()

    class Meta:
        model=Product
        fields= '__all__'

    def get_images(self, obj):
        return obj.get_images_urls()
