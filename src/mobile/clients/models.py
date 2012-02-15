from django.db import models
from mobile.lib import fields
# Create your models here.

class Client(models.model):
    id = fields.UUIDField(primary_key=True)
    client_name = models.CharField(max_length=100, null=False, blank=True)
    username = models.CharField(max_length=30, null=False, blank=True)
    password = models.CharField(max_length=20, null=False, blank=True)
    secret = models.CharField(max_length=150, null=False, blank=True)

