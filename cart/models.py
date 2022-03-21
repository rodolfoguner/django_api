from django.db import models
from client.models import Client
from product.models import Product
from django.db.models.signals import pre_save, post_save, m2m_changed


class Cart(models.Model):
    owner = models.ForeignKey(Client,related_name='carts', on_delete=models.CASCADE)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    products = models.ManyToManyField(Product, related_name='products')

    def __str__(self):
        return f'{self.owner}'


def m2m_changed_cart_total(sender, instance, action, *args, **kwargs):
  if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
    products = instance.products.all() 
    total = 0 
    for product in products: 
      total += product.price 
    instance.total = total
    instance.save()

m2m_changed.connect(m2m_changed_cart_total, sender = Cart.products.through)

