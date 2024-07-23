from django.db import models

class Order(models.Model):
    description = models.CharField(max_length=200)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.question_text