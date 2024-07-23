from django.db import models
import json
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from .consumers import OrderConsumer

class Order(models.Model):
    description = models.CharField(max_length=200)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{} {}".format(self.name, self.description)
    

    def save(self, *args, **kwargs):
        print('in save',self)
        order_obj = {}
        channel_layer = get_channel_layer()
        super(Order, self).save(*args, **kwargs)
        async_to_sync(channel_layer.group_send)('orders', {
            'type': 'new.order',
            'content': self
        })


        