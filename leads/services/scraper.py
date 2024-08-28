from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import environ
import time
from selenium.webdriver.common.action_chains import ActionChains
from dataclasses import dataclass
from leads.models import Account
from django.conf import settings
from datetime import datetime
from dateutil.parser import parse
import os

from leads.services.email_sender import EmailSender

@dataclass
class ScrapedLead:
  account_name: str
  customer_name: str
  date: str
  first_call_time: str
  total_talk_time: str
  call_date_time: datetime
  initial_status_date_time: datetime
  won_job_status_date_time: datetime
  job_fee: str

  def __str__(self):
    return f'{self.date} - {self.customer_name} - Time to First Call: {self.first_call_time}, Total Talk Time: {self.total_talk_time}'

class Scraper:
  env = environ.Env(
    GOOGLE_CHROME_SHIM=(str, '/usr/bin/google-chrome'),
    # NOTE this chromedriver only works on linux locally right now!
    CHROMEDRIVER_PATH=(str, './resources/chromedriver')
  )

  GOOGLE_CHROME_PATH = env('GOOGLE_CHROME_SHIM')
  CHROMEDRIVER_PATH = env('CHROMEDRIVER_PATH')

  LOGIN = settings.SCRAPER_LOGIN_URL
  LEADS = settings.SCRAPER_LEADS_URL
    
  @staticmethod
  def scrape(date) -> list[ScrapedLead]:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--enable-javascript")
    chrome_options.binary_location = Scraper.GOOGLE_CHROME_PATH

    driver = webdriver.Chrome(executable_path=Scraper.CHROMEDRIVER_PATH, chrome_options=chrome_options)

    accounts = Account.objects.filter(active = True)

    leads: list[ScrapedLead] = []

    for account in accounts:
      account_name = account.account_name
      username = account.user_name
      pw = account.account_pass

      driver.get(Scraper.LOGIN)

      username_field = driver.find_element(By.ID, 'username')
      username_field.send_keys(username)
      pass_field = driver.find_element(By.ID, 'password')
      pass_field.send_keys(pw)
      pass_field.send_keys(Keys.RETURN)

      time.sleep(15)

      driver.get(Scraper.LOGIN)

      username_field = driver.find_element(By.ID, 'username')
      username_field.send_keys(username)
      pass_field = driver.find_element(By.ID, 'password')
      pass_field.send_keys(pw)
      pass_field.send_keys(Keys.RETURN)

      time.sleep(3)

      body = driver.find_element(By.TAG_NAME, 'body')
      print(body.get_attribute('innerHTML')[:3000])

      print(f'{account_name} successfully logged in')

      driver.get(Scraper.LEADS)
      driver.implicitly_wait(3)
      time.sleep(3)

      # get html body and print first 800 characters
      body = driver.find_element(By.TAG_NAME, 'body')
      print(body.get_attribute('innerHTML')[:800])

      dates = [date]
      print(f'On Active Leads page, getting leads for these dates: {dates}')
      old_date_found = False

      start = time.time()

      skip_account = False
      second_try = False

      while not old_date_found:
        curr = time.time()
        if (curr - start >= 30) and not second_try:
          print("Taking too long, reloading leads page once.")
          second_try = True
          driver.get(Scraper.LEADS)
          driver.implicitly_wait(3)
          time.sleep(3)
        
        if (curr - start) >= 70 and second_try:
          print("Taking too long, there was a problem scraping account " + account_name + ". Moving onto the next account.")
          driver.delete_all_cookies()
          skip_account = True
          break

        lead_els = driver.find_elements_by_xpath("//div[@id='pipe-leads']/div")
        print(f'Found {len(lead_els)} leads currently on page')

        for lead_el in lead_els:
          children = lead_el.find_elements_by_xpath(".//*")
          dateDiv = children[11]
          old_date_found = dateDiv.text not in dates

        if not old_date_found:
          print("Scrolling for more leads for given date(s)")
          driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
          time.sleep(2)
        
      if skip_account:
        continue

      curr_lead_els = []

      for lead_el in lead_els:
        children = lead_el.find_elements_by_xpath(".//*")
        dateDiv = children[11]
        if dateDiv.text in dates:
          curr_lead_els.append(lead_el)

      if len(curr_lead_els) > 0:
        print(f'{len(curr_lead_els)} leads for given date(s) found. Extracting data.')

        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(3)

        for lead_el in curr_lead_els:  
          children = lead_el.find_elements_by_xpath(".//*")
          name = children[4].text
          print(f'Extracting data for lead {name}')
          date = children[11].text
          lead_el.click()
          time.sleep(5)
          history_text = driver.find_element_by_xpath("//div[contains(@class, 'lead-tab') and contains(@class, 'history')]").get_attribute("innerText")
          initial_status_date_time = Scraper._get_status_date_time(driver, "Initial")
          won_job_status_date_time = Scraper._get_status_date_time(driver, "Won Job")
          job_fee = Scraper._get_job_fee(driver)
          call_date_time = None
          if "You have not contacted this customer" in history_text:
            first_call_time = 'N/A'
            total_talk_time = 'N/A'
          else:
            call_stats = driver.find_elements_by_xpath("//div[contains(@class, 'lead-tab') and contains(@class, 'history')]//div[@class='stat-data']")
            if call_stats and len(call_stats) > 2:
                first_call_time = call_stats[0].get_attribute("innerText")
                total_talk_time = call_stats[2].get_attribute("innerText")
                call_date_time = Scraper._get_call_date_time(driver)
            else:
                first_call_time = 'N/A'
                total_talk_time = 'N/A'
          
          leads.append(ScrapedLead(
            account_name, 
            name, 
            date, 
            first_call_time, 
            total_talk_time, 
            call_date_time, 
            initial_status_date_time,
            won_job_status_date_time,
            job_fee))
      else:
        print("No leads for given date(s). Skipping.")

      driver.delete_all_cookies()

    driver.quit()

    return leads

  def _get_job_fee(driver):
    job_fee_xpath = ("//div[contains(@class, 'lead-tab') and contains(@class, 'details')]")
    detail_els = driver.find_elements_by_xpath(job_fee_xpath)
    if detail_els and len(detail_els) > 0:
      children = detail_els[0].find_elements_by_xpath(".//*")
      for child in children:
        if "Job Fee" in child.get_attribute("innerText"):
          if "$" in child.get_attribute("innerText"):
            return child.get_attribute("innerText").split("$")[1].strip()
    return None

  # must be on leads page with lead selected for this function to work
  def _get_status_date_time(driver, status_type):
    status_change_xpath = ("//div[contains(@class, 'lead-tab') and contains(@class, 'history')]"
                            "//div[contains(@class, 'history-wrapper') and contains(@class, 'status-change')]")
    status_change_els = driver.find_elements_by_xpath(status_change_xpath)
    if status_change_els:
      for el in status_change_els:
        children = el.find_elements_by_xpath(".//*")
        if status_type in children[1].get_attribute("innerText"):
          return parse(children[0].get_attribute("innerText").replace("| ", ""))
    return None

  # must be on leads page with lead selected for this function to work
  def _get_call_date_time(driver):
    call_time_xpath = ("//div[contains(@class, 'lead-tab') and contains(@class, 'history')]"
                       "//div[contains(@class, 'history-wrapper') and contains(@class, 'call')]")
    call_time_els = driver.find_elements_by_xpath(call_time_xpath)
    call_time_el = call_time_els[-1] if call_time_els and len(call_time_els) > 0 else None
    if call_time_el:
      call_time_children = call_time_el.find_elements_by_xpath(".//*")
      if call_time_children and len(call_time_children) > 0:
        call_time_str = call_time_children[0].get_attribute("innerText").replace("| ", "")
        return parse(call_time_str)
    return None