from django.db import models
from mobile.lib import fields
# Create your models here.


class SmsTransactions(models.Model):
    id = fields.UUIDField(primary_key=True)
    user_pmt_id = models.ForeignKey(UserPayment, blank=True, null=True)
    user_id = models.ForeignKey(Users, blank=True, null=True) 
    client_id = models.ForeignKey(Client, blank=True, null=True) 
    name = models.CharField(max_length=100)
    data = JSONObjectField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    rsp = models.CharField(max_length=600)