from leads.services.HAScraper import ScrapedLead
from leads.models import Lead
from dateutil.parser import parse


class LeadRepository:
        
    @staticmethod
    def save_leads(scraped_leads: list[ScrapedLead]):
        for scraped_lead in scraped_leads:
            
            user_name = scraped_lead.user 
            display_name = scraped_lead.name
            first_call_time = scraped_lead.first_call_time
            total_talk_time = scraped_lead.total_talk_time
            created_date = parse(scraped_lead.date)

            Lead.objects.create(
                user_name=user_name, 
                display_name=display_name, 
                first_call_time=first_call_time, 
                total_talk_time=total_talk_time, 
                created_date=created_date,)