from django.db import models

class Leads(models.Model):
    user_name = models.CharField(max_length=100)
    first_call_time = models.IntegerField(max_length= 5)
    total_talk_time = models.IntegerField(max_length= 5)
    date = models.DateTimeField()
