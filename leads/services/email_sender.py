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

        print("Recipients: " + str(recs))
        # print("Content: " + rendered_content)

        send_mail(
            message.title,
            '', 
            sender,
            recs,
            html_message=rendered_content,
        )
        print('Mail has been sent') 
        