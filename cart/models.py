from django.db import models
from order.models import Order, OrderItem
from product.models import Product
from user_profile.models import UserProfile
# Create your models here.
from util.models import BaseModel

class Cart(BaseModel):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    
    def order(self):
        all_cart_items = self.items.all()
        order = Order.objects.create(profile=self.profile)
        for cart_item in all_cart_items:
            OrderItem.objects.create(
               order=order,
               product=cart_item.product,
               quantity=cart_item.quantity
            )
        all_cart_items.delete()

    @property
    def total(self):
        return sum(item.total for item in self.items.all())

class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Quantity')

    def __str__(self) -> str:
        return f'{self.product.name} - {self.cart.profile.user.username}'

    @property
    def total(self):
        return self.quantity * self.product.price