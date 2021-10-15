from django.db import models


class Lead(models.Model):
    user_name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100)
    first_call_time = models.CharField(max_length= 5)
    total_talk_time = models.CharField(max_length= 5)
    created_date = models.DateTimeField()


    def __str__(self):
        return self.user_name