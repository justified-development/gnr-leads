from models import Leads


class Save_DB:
    def __init__(self):
        lead_name = Leads.objects.lead_name.all()
        first_call_time = Leads.objects.first_call_time.all()
        total_talk_time = Leads.objects.total_talk_time.all()

    def __str__(self):
        return self.lead_name

    def __str__(self):
        return self.first_call_time

    def __str__(self):
        return self.total_talk_time