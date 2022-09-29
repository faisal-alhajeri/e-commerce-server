from .models import Product, ProductCategory, ProductImage
from rest_framework.serializers import  ModelSerializer, SerializerMethodField

class ProductImageSerializer(ModelSerializer):
    url = SerializerMethodField()

    class Meta:
        model=ProductImage
        fields= ['uuid', 'url']

    def get_url(self, obj):
        return obj.img.url

class ProductCategorySerializer(ModelSerializer):

    class Meta:
        model=ProductCategory
        fields= ['name' , 'uuid']


class ProductSerializer(ModelSerializer):
    mainImageUrl = SerializerMethodField()
    images = ProductImageSerializer(many=True)

    categories = ProductCategorySerializer(many=True)

    class Meta:
        model=Product
        fields= '__all__'


    def get_mainImageUrl(self, obj):
        return obj.get_main_image_url()


