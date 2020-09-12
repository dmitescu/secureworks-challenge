from django.db import models

NA = "N/A"

class IntrusionAttempt(models.Model):
    intrusion_type = models.CharField(max_length=1)
    subnet = models.CharField(max_length=32, default=NA)
