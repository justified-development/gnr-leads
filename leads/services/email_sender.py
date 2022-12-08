from leads.models import Lead  
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from leads.models import Message

from mailersend import emails

class EmailSender:

    @staticmethod
    def send_email(date):
        leads = Lead.objects.filter(run_date = date).order_by('account_name', 'initial_lead_date_time', 'won_job_date_time')
        # print(leads)
        sender = settings.EMAIL_HOST_USER
        receiver = settings.EMAIL_RECIPIENT
        recs = receiver.split(',') if ',' in receiver else [receiver]

        messages = Message.objects.filter(active = True)
        if len(messages) == 0:
            raise Exception("No active Messages in DB")
        if len(messages) > 1:
            print("Warning: multiple Message records. Just using the first.")
        message = messages[0]

        rendered_content = render_to_string('email.html', { "leads": leads, "prelude": message.prelude, "today": date})


        # assigning NewEmail() without params defaults to MAILERSEND_API_KEY env var
        mailer = emails.NewEmail()

        # define an empty dict to populate with mail values
        mail_body = {}

        mail_from = {
            "name": "Dev",
            "email": "dev@justdev.us",
        }

        recipients = [
            {
                "name": "Dev",
                "email": "dev@justdev.us",
            }
        ]

        reply_to = [
            {
                "name": "Dev",
                "email": "dev@justdev.us",
            }
        ]

        mailer.set_mail_from(mail_from, mail_body)
        mailer.set_mail_to(recipients, mail_body)
        mailer.set_subject(message.title, mail_body)
        mailer.set_html_content(rendered_content, mail_body)
        # mailer.set_plaintext_content(rendered_content, mail_body)
        mailer.set_reply_to(reply_to, mail_body)

        try:
            # using print() will also return status code and data
            print(mailer.send(mail_body))
        except Exception as e:
            print(e)