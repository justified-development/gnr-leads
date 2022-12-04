from leads.services.scraper import Scraper, ScrapedLead
from leads.services.lead_repository import LeadRepository
from datetime import datetime, timedelta
from leads.services.email_sender import EmailSender

def run(*args):
  yesterday = datetime.today() - timedelta(days=1)
  date_string = yesterday.strftime('%-m/%-d/%Y')
  yesterday2 = datetime.today() - timedelta(days=2)
  date_string2 = yesterday2.strftime('%-m/%-d/%Y')
  yesterday3 = datetime.today() - timedelta(days=3)
  date_string3 = yesterday3.strftime('%-m/%-d/%Y')
  yesterday4 = datetime.today() - timedelta(days=4)
  date_string4 = yesterday4.strftime('%-m/%-d/%Y')
  leads: list[ScrapedLead] = Scraper.scrape([date_string, date_string2, date_string3, date_string4])
  print(leads)
  LeadRepository.save_leads(leads)
  EmailSender.send_email(yesterday)
  