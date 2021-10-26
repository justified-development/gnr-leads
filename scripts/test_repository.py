from leads.services.lead_repository import LeadRepository 
from leads.services.scraper import ScrapedLead
from leads.models import Lead

def run(*args):
    scraped_leads = []
    scraped_leads.append(ScrapedLead('Illinois', 'test_username', '10/25/2021', '5m 0s', '10m 0s'))
    scraped_leads.append(ScrapedLead('Arizona', 'test_username2', '10/25/2021', '7m 0s', '12m 0s'))

    LeadRepository.save_leads(scraped_leads)

    saved_leads = Lead.objects.all()
    assert 2 == len(saved_leads)

    # Lead.objects.all().delete
    