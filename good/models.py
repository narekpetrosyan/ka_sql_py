from django.db import models
from storage.models import Storage


class Good(models.Model):
    GoodName = models.CharField(max_length=50)
    GoodDescription = models.CharField(max_length=200, blank=True, null=True)
    GoodCategory = models.CharField(max_length=50)
    GoodQuantity = models.IntegerField()
    GoodBrand = models.CharField(max_length=50, blank=True, null=True)
    GoodPrice = models.DecimalField(max_digits=10, decimal_places=2)
    StorageID = models.ForeignKey(to=Storage, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.GoodName
