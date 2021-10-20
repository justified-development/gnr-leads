from leads.services.email_data import EmailSender

def run(*args):
  date = '2021-10-02'
  EmailSender.send_email(date)
  # this is just an example