from leads.services.HAScraper import HAScraper, Lead

def run(*args):
  date = '10/2/2021'
  leads: list[Lead] = HAScraper.scrape(date)
  print(leads)
  