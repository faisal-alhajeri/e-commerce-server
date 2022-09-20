from django.db import models

from util.models import BaseModel
from versatileimagefield.fields import VersatileImageField

# Create your models here.

class Product(BaseModel): 
    name = models.CharField('Product Name',max_length=255)
    description = models.TextField()
    price = models.DecimalField('Product Price', max_digits=4, decimal_places=1)

    def get_images_urls(self):
        images = self.images.all()
        if images:
            return [imgObj.img.url for imgObj in images]
        else:
            return ['static/images/default.png']

    def __str__(self) -> str:
        return f'{self.name} - {self.uuid}'

class ProductImage(BaseModel): 
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    img = VersatileImageField()

    def __str__(self) -> str:
        return f'{self.product.name} - {self.uuid}'