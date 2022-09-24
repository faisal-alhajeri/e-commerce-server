from .models import Product, ProductCategory
from rest_framework.serializers import  ModelSerializer, SerializerMethodField

class ProductCategorySerializer(ModelSerializer):

    class Meta:
        model=ProductCategory
        fields= ['name' , 'uuid']


class ProductSerializer(ModelSerializer):
    images = SerializerMethodField()
    categories = ProductCategorySerializer(many=True)

    class Meta:
        model=Product
        fields= '__all__'

    def get_images(self, obj):
        return obj.get_images_urls()


