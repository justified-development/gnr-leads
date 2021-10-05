from HAScraper import ScrapedLead
from HAScraper import HAScraper
# TODO: should get renamed to Lead
from models import Leads

# TODO: refactor
# I see where you were going with this, but this class should actually take in a list of leads instead of
# just one, and it also needs to have a function to call - it will never hit line 31 because it's not
# the entry point of the app. Below the class I've stubbed out a class that you can work off of.
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


# TODO: delete the above class and implement the below class
# TODO: rename file to lead_repository.py
# a repository is a class that interacts with a database essentially
class LeadRepository:
    # no init needed because we will be using static methods
    # static methods can be called on a class like this: LeadRepository.save_leads()
    # you don't need to instantiate the class first
    # TODO: implement this method. It takes a list of ScrapedLead objects, converts them into Lead models,
    # and saves them to the DB
    @staticmethod
    def save_leads(scraped_leads: list[ScrapedLead]):
        # for each ScrapedLead object in the given list, convert it to a Lead model
        # then for each Lead model, call save() on it
        pass