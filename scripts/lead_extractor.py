from leads.services.scraper import Scraper, ScrapedLead
from leads.services.lead_repository import LeadRepository
from datetime import datetime
from leads.services.email_sender import EmailSender

def run(*args):
  today = datetime.today()
  date = datetime.today().strftime('%m/%d/%Y')
  leads: list[ScrapedLead] = Scraper.scrape(date)
  print(leads)
  LeadRepository.save_leads(leads)
  EmailSender.send_email(today)
  