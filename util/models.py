from django.db import models
from django.utils import timezone
import uuid

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField('created at', default=timezone.now)
    modified_at = models.DateTimeField('modified at', default=timezone.now)
    uuid = models.UUIDField( primary_key = True, default =uuid.uuid4, editable = False)

    class Meta:
        abstract = True
