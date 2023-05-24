from django.contrib import admin
from storage.models import Storage


class StorageAdmin(admin.ModelAdmin):
    list_display = ('id', 'StorageName', 'Address', 'Country', 'State',
                    'City', 'Phone', 'Capacity')


admin.site.register(Storage, StorageAdmin)
