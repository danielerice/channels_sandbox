from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)
        #here is where I will send the signal to the websocket