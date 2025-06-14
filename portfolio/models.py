from django.db import models
from django.utils import timezone
from django.utils.timezone import localtime


class VisitorLog(models.Model):
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        local_time = localtime(self.timestamp)
        return f"{self.ip_address} at {local_time.strftime('%Y-%m-%d %H:%M:%S %Z')}"
