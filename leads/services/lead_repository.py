from leads.services.HAScraper import ScrapedLead
from leads.models import Lead
from dateutil.parser import parse


class LeadRepository:
        
    @staticmethod
    def save_leads(scraped_leads: list[ScrapedLead]):
        for scraped_lead in scraped_leads:
            # for l in lead:
            user_name = scraped_lead.user # swap these
            display_name = scraped_lead.name
            first_call_time = scraped_lead.first_call_time
            total_talk_time = scraped_lead.total_talk_time
            created_date = parse(scraped_lead.date) # parse this

            Lead.objects.create(
                user_name=user_name, 
                display_name=display_name, 
                first_call_time=first_call_time, 
                total_talk_time=total_talk_time, 
                created_date=created_date)

            # LeadRepository.save_leads.user_name.save()
            # LeadRepository.save_leads.display_name.save()
            # LeadRepository.save_leads.first_call_time.save()
            # LeadRepository.save_leads.total_talk_time.save()
            # LeadRepository.save_leads.created_date.save()
    