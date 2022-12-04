from leads.services.scraper import Scraper, ScrapedLead
from leads.services.lead_repository import LeadRepository
from datetime import datetime, timedelta
from leads.services.email_sender import EmailSender

def run(*args):
  yesterday = datetime.today() - timedelta(days=1)
  date_string = yesterday.strftime('%-m/%-d/%Y')
  leads: list[ScrapedLead] = Scraper.scrape(date_string)
  print(leads)
  LeadRepository.save_leads(leads)
  EmailSender.send_email(yesterday)
  