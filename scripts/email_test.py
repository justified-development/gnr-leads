from leads.services.email_sender import EmailSender
from django.utils import timezone
from datetime import datetime

def run(*args):
  # date = '2021-10-26'
  EmailSender.send_email([datetime.today()])
# EmailSender.send_email(date)
