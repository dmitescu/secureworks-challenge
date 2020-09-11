from django.db import models

import uuid

class Downtime(models.Model):
    deployment_id = models.PositiveIntegerField()
    date = models.DateTimeField()
    duration = models.PositiveIntegerField()
