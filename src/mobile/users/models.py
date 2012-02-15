from django.db import models

# Create your models here.


class User(models.model):
    id = fields.UUIDField(primary_key=True) 
