from leads.services.scraper import Scraper, ScrapedLead
from leads.services.lead_repository import LeadRepository
from datetime import datetime, timedelta
from leads.services.email_sender import EmailSender
from django.conf import settings

def run(*args):
  currDays = '1'
  if len(args) > 0:
    currDays = args[0]
  
  if ',' in currDays:
    # map currDays comma separated string to array of ints
    currDaysArr = list(map(int, currDays.split(',')))
  else:
    currDaysArr = [int(currDays)]

  datetimes = []
  if (len(args) < 2 or args[1] != "skip_scrape"):
    for currDays in currDaysArr:
      yesterday = datetime.today() - timedelta(days=currDays)
      datetimes.append(yesterday)
      date_string = yesterday.strftime('%-m/%-d/%Y')
      if not settings.SKIP_SCRAPE == "true":
        leads: list[ScrapedLead] = Scraper.scrape(date_string)
        print(leads)
        LeadRepository.save_leads(leads)

  if (len(args) < 2 or args[1] != "skip_email"):
    EmailSender.send_email(datetimes)
  