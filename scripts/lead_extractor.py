from leads.services.scraper import Scraper, ScrapedLead
from leads.services.lead_repository import LeadRepository
from datetime import datetime, timedelta
from leads.services.email_sender import EmailSender
from django.conf import settings

def run(*args):
  currDays = 1
  if len(args) > 0:
    currDays = int(args[0])

  yesterday = datetime.today() - timedelta(days=currDays)
  date_string = yesterday.strftime('%-m/%-d/%Y')
  if not settings.SKIP_SCRAPE == "true":
    leads: list[ScrapedLead] = Scraper.scrape(date_string)
    print(leads)
    LeadRepository.save_leads(leads)
  EmailSender.send_email(yesterday)
  