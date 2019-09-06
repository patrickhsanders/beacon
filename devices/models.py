from django.db import models
import uuid

# Create your models here.

class Device(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    checkin_identifier = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name