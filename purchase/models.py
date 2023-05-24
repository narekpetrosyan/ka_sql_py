from django.db import models
from good.models import Good
from customer.models import Customer


class Purchase(models.Model):
    PurchaseDate = models.DateField(auto_now=True)
    PurchaseQuantity = models.IntegerField()
    PurchasePrice = models.DecimalField(max_digits=10, decimal_places=2)
    GoodID = models.ForeignKey(to=Good, on_delete=models.CASCADE)
    CustomerID = models.ForeignKey(to=Customer, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return str(self.PurchaseDate)
