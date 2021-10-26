from leads.services.email_data import EmailSender
from django.utils import timezone

def run(*args):
  date = '2021-10-25'
  EmailSender.send_email(date)
  # this is just an example