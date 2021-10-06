from HAScraper import ScrapedLead




class LeadRepository:
        
    @staticmethod
    def save_leads(scraped_leads: list[ScrapedLead]):
        for i in scraped_leads:
            lead = i
            for l in lead:
                user_name = user
                display_name = name
                first_call_time = first_call_time
                total_talk_time = total_talk_time
                created_date = date

                LeadRepository.save_leads.user_name.save()
                LeadRepository.save_leads.display_name.save()
                LeadRepository.save_leads.first_call_time.save()
                LeadRepository.save_leads.total_talk_time.save()
                LeadRepository.save_leads.created_date.save()
    