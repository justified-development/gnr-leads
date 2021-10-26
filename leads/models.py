from django.db import models

class Lead(models.Model):
    account_name = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    first_call_time = models.CharField(max_length= 20)
    total_talk_time = models.CharField(max_length= 20)
    created_date = models.DateTimeField()

    def __str__(self):
        return f'{self.account_name}: {self.created_date} - {self.customer_name} - Time to First Call: {self.first_call_time}, Total Talk Time: {self.total_talk_time}'

class Message(models.Model):
    title = models.CharField(max_length=500)
    prelude = models.CharField(max_length=500)
    active = models.BooleanField(default=False)

class Account(models.Model):
    account_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    active = models.BooleanField(default=False)