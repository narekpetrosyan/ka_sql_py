from django.db import models


class Customer(models.Model):
    CustomerName = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.CustomerName
