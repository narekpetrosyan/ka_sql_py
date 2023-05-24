from django.db import models


class Storage(models.Model):
    StorageName = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    Country = models.CharField(max_length=50, blank=True, null=True)
    State = models.CharField(max_length=50, blank=True, null=True)
    City = models.CharField(max_length=50, blank=True, null=True)
    Phone = models.CharField(max_length=20, blank=True, null=True)
    Capacity = models.DecimalField(
        blank=True, null=True, max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.StorageName
