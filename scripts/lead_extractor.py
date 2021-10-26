from leads.services.HAScraper import HAScraper, ScrapedLead
from leads.services.lead_repository import LeadRepository

def run(*args):
  date = '10/26/2021'
  leads: list[ScrapedLead] = HAScraper.scrape(date)
  print(leads)
  # TODO: nothing to do here, just note that this is how we will use your new class
  LeadRepository.save_leads(leads)
  