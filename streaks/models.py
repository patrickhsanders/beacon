from django.db import models
from devices.models import Device

# Create your models here.


class Streak(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    device = models.ForeignKey(Device)
    ip_address = models.GenericIPAddressField(blank=False, null=False)