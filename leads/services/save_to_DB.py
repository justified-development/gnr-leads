from HAScraper import Lead


class Save_DB(Lead):
    def __init__(self, user, name, date, first_call_time, total_talk_time):
        self.user = user
        self.name = name
        self.date = date
        self.first_call_time = first_call_time
        self.total_talk_time = total_talk_time

    def sav_user(self, user):
        user.save()

    def sav_user(self, name):
        name.save()

    def sav_user(self, date):
        date.save()

    def sav_user(self, first_call_time):
        first_call_time.save()

    def sav_user(self, total_talk_time):
        total_talk_time.save()

    