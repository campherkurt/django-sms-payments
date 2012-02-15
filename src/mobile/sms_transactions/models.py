from django.db import models

# Create your models here.


class SmsTransactions(models.Model):
    id = fields.UUIDField(primary_key=True)
    user_pmt_id = fields.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    data = JSONObjectField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    user_id = models.ForeignKey(Users, blank=True, null=True) 
    rsp = models.CharField(max_length=400)

   
