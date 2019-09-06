from django.db import models
from devices.models import Device
from streaks.models import Streak
# Create your models here.


class Checkin(models.Model):
    device = models.ForeignKey(Device, null=False, blank=False)
    ip_address = models.GenericIPAddressField(null=False, blank=False)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    streak = models.ForeignKey(Streak, null=False, blank=False)
