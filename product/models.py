from django.db import models

from util.models import BaseModel
from versatileimagefield.fields import VersatileImageField

# Create your models here.
class ProductCategory(BaseModel):
    name = models.CharField("Product Category", max_length=55)


    def __str__(self) -> str:
        return f'category - {self.name} - {self.uuid}'


class Product(BaseModel): 
    name = models.CharField('Product Name',max_length=255)
    description = models.TextField()
    price = models.DecimalField('Product Price', max_digits=4, decimal_places=1)
    categories = models.ManyToManyField(ProductCategory, related_name='products', null=True, blank=True)

    def get_main_image_url(self):
        images = self.images.all()
        if images:
            return images.first().img.url
        else:
            return 'static/images/default.png'


    def __str__(self) -> str:
        return f'{self.name} - {self.uuid}'

    def add_images(self, files):
        for image_name in files: 
            self.images.create(img=files[image_name])

class ProductImage(BaseModel): 
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    img = VersatileImageField()

    def __str__(self) -> str:
        return f'{self.product.name} - {self.uuid}'


