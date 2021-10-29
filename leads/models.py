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
    def time_string_as_sec(time_string):
        split_time = time_string.strip().split(' ')
        total_time = 0
        for segment in split_time:
            if 'd' in segment:
                total_time = total_time + (int(segment.replace('d', '')) * 24 * 60 * 60)
            elif 'h' in segment:
                total_time = total_time + (int(segment.replace('h', '')) * 60 * 60)
            elif 'm' in segment:
                total_time = total_time + (int(segment.replace('m', '')) * 60)
            elif 's' in segment:
                total_time = total_time + int(segment.replace('s', ''))
        return total_time

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