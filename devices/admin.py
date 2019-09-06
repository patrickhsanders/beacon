from django.contrib import admin
from .models import Device


class DeviceAdmin(admin.ModelAdmin):
    fields = ('name', 'checkin_identifier', )
    readonly_fields = ('checkin_identifier', )


admin.site.register(Device, DeviceAdmin)