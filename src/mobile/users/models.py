from django.db import models
from mobile.lib import fields
# Create your models here.


class User(models.model):
    id = fields.UUIDField(primary_key=True) 
    phone_number = models.CharField(max_length=20)
    origin_client_id = models.ForeignKey(Client, blank=True, null=True) 
    date_created = models.DateTimeField(blank=True, null=True)
    
