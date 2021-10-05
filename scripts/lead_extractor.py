from leads.services.HAScraper import HAScraper, ScrapedLead

def run(*args):
  date = '10/2/2021'
  leads: list[ScrapedLead] = HAScraper.scrape(date)
  print(leads)
  # this is where we would pass the leads into another class that would save to DB