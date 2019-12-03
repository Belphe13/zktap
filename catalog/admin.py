from django.contrib import admin
from .models import Door


# Register your models here.
class DoorAdmin(admin.ModelAdmin):
    list_display = ('door_name', 'location', 'door_public_key')
    search_fields = ['door_name']


# admin.site.register(User)
admin.site.register(Door, DoorAdmin)
