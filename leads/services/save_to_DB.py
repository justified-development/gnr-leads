from HAScraper import Lead
from HAScraper import HAScraper


class Save_DB:
    def __init__(self, user, name, date, first_call_time, total_talk_time):
        self.user = user
        self.name = name
        self.date = date
        self.first_call_time = first_call_time
        self.total_talk_time = total_talk_time

    def sav_user(self, user):
        user.save()

    def sav_name(self, name):
        name.save()

    def sav_date(self, date):
        date.save()

    def sav_time(self, first_call_time):
        first_call_time.save()

    def sav_talk_time(self, total_talk_time):
        total_talk_time.save()

for i in HAScraper.leads:
    Save_DB(i)