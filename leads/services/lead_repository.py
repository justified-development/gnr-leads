from leads.services.scraper import ScrapedLead
from leads.models import Lead
from dateutil.parser import parse
from datetime import datetime
from django.utils.timezone import make_aware

class LeadRepository:
        
    @staticmethod
    def save_leads(scraped_leads: list[ScrapedLead]):
        for scraped_lead in scraped_leads:

            account_name = scraped_lead.account_name 
            customer_name = scraped_lead.customer_name
            first_call_time = scraped_lead.first_call_time
            total_talk_time = scraped_lead.total_talk_time
            run_date = parse(scraped_lead.date)
            created_date = make_aware(datetime.now())
            call_date_time = make_aware(scraped_lead.call_date_time) if scraped_lead.call_date_time else None

            initial_lead_date_time = Lead.calculate_initial_lead_time(call_date_time, first_call_time)

            Lead.objects.create(
                account_name=account_name, 
                customer_name=customer_name, 
                first_call_time=first_call_time, 
                total_talk_time=total_talk_time, 
                call_date_time=call_date_time,
                initial_lead_date_time=initial_lead_date_time,
                created_date=created_date,
                run_date=run_date)