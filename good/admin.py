from django.contrib import admin
from good.models import Good


class GoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'GoodName', 'GoodDescription', 'GoodCategory',
                    'GoodQuantity', 'GoodBrand', 'GoodPrice')


admin.site.register(Good, GoodAdmin)
