from django.db import models
from product.models import Product
from user_profile.models import UserProfile
# Create your models here.
from util.models import BaseModel

class CartItem(BaseModel):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Quantity')

    def __str__(self) -> str:
        return f'{self.product.name} - {self.profile.user.username}'