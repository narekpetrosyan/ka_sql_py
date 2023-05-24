from django.contrib import admin
from purchase.models import Purchase


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'PurchaseDate',
                    'PurchaseQuantity',
                    'PurchasePrice')


admin.site.register(Purchase, PurchaseAdmin)
