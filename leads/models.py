from django.db import models

# TODO: 
# rename to Lead
# add display_name field (string)
# make first_call_time and total_talk_time strings for simplicity
# rename date to created_date
class Leads(models.Model):
    user_name = models.CharField(max_length=100)
    first_call_time = models.IntegerField(max_length= 5)
    total_talk_time = models.IntegerField(max_length= 5)
    date = models.DateTimeField()
