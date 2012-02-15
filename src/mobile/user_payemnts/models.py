from django.db import models
from mobile.lib import fields
# Create your models here.

class UserPayments(models.model):
    id = fields.UUIDField(primary_key=True)
    user_id = models.ForeignKey(Users, blank=True, null=True)
    client_id = models.ForeignKey(Client, blank=True, null=True)
    amount = models.DecimalField(max_digits=15,decimal_places=2,blank=True,null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    data = JSONObjectField(blank=True, null=True)
