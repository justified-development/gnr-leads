from django.db import models
import datetime

class Lead(models.Model):
    account_name = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    # first_call_time and total_talk_time strings look like '1m 12s' or '12s'
    first_call_time = models.CharField(max_length= 20)
    total_talk_time = models.CharField(max_length= 20)
    call_date_time = models.DateTimeField(null=True)
    initial_lead_date_time = models.DateTimeField(null=True)
    won_job_date_time = models.DateTimeField(null=True)
    job_fee = models.CharField(max_length=10, null=True)
    run_date = models.DateField()
    created_date = models.DateTimeField()

    def __str__(self):
        return f'{self.account_name}: {self.run_date} - {self.customer_name} - Time to First Call: {self.first_call_time}, Total Talk Time: {self.total_talk_time}'

    @staticmethod
    def time_string_as_sec(first_call_time):
        split_call_time = first_call_time.strip().split(' ') if ' ' in first_call_time.strip() else [first_call_time.strip()]
        if len(split_call_time) == 1:
            return int(split_call_time[0].replace('s', ''))
        else:
            mins = int(split_call_time[0].replace('m', ''))
            return int(split_call_time[1].replace('s', '')) + (mins * 60)

    @staticmethod
    def calculate_initial_lead_time(call_date_time, first_call_time):
        if not call_date_time:
            return None
        return call_date_time - datetime.timedelta(seconds=Lead.time_string_as_sec(first_call_time))

class Message(models.Model):
    title = models.CharField(max_length=500)
    prelude = models.CharField(max_length=500)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

class Account(models.Model):
    account_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    account_pass = models.CharField(max_length=50)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.account_name}'