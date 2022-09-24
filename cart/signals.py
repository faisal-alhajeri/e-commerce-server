from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from cart.models import CartItem





@receiver(post_save, sender=CartItem)
def delete_empty_cart_item(instance, **kwargs):
    cart_item: CartItem = instance
    if cart_item.quantity == 0:
        cart_item.delete()

