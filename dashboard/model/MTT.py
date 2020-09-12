from django.db import models
import uuid

NA = "N/A"

class MTTD(models.Model):
    ticket_id = models.PositiveIntegerField() # should be a foreign key
    department = models.CharField(max_length=32, default=NA)
    duration = models.PositiveIntegerField()

class MTTR(models.Model):
    ticket_id = models.PositiveIntegerField() # should be a foreign key
    department = models.CharField(max_length=32, default=NA)
    duration = models.PositiveIntegerField()

    
