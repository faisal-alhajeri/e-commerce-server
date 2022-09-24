

from django.db import models
from user_profile.models import UserProfile
from product.models import Product
# Create your models here.
from util.models import BaseModel

class Order(BaseModel):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.profile} - {self.uuid}'

    @property
    def total(self):
        return sum(item.total for item in self.items.all())

    @classmethod
    def user_orders(cls, user):
        return cls.objects.filter(profile=user.profile).order_by('-created_at')

    


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Quantity')


    def __str__(self) -> str:
        return f'{self.order} - {self.product.name}'
    
    @property
    def total(self):
        return self.quantity * self.product.price