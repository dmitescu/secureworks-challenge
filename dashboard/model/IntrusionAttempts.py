from django.db import models

class IntrusionAttempt(models.Model):
    intrusion_type = models.CharField(max_length=1)
    date = models.DateTimeField()
