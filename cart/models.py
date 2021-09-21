from django.db import models
from django.db.models.fields import FloatField
from django.db.models.signals import pre_save, post_save, m2m_changed
from client.models import Client
from product.models import Product


class Cart(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    product = models.ManyToManyField(Product)


    def __str__(self):
        return self.id


def  m2m_changed_cart_total(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear' or action == 'pre_save':
        list_product = instance.Product.all() 
    total = 0 
    for p in list_product: 
        total += p.price 
    instance.save()

m2m_changed.connect(m2m_changed_cart_total, sender = Cart.product.through)
