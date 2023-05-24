from django.contrib import admin
from customer.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'CustomerName', 'Address')


admin.site.register(Customer, CustomerAdmin)
