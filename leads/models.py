from django.db import models

class Leads(models.Model):
    lead_name = models.CharField(max_length=100)
    first_call_time = models.IntegerField(max_length= 5)
    total_call_time = models.IntegerField(max_length= 5)
    time_created = models.DateTimeField()
