from django.db import models
import uuid

class MTTD(models.Model):
    ticket_id = models.UUIDField(default=uuid.uuid4, editable=False) # should be a foreign key
    duration = models.PositiveIntegerField()

class MTTR(models.Model):
    ticket_id = models.UUIDField(default=uuid.uuid4, editable=False) # should be a foreign key
    duration = models.PositiveIntegerField()

    
