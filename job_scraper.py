from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import datetime
import time

print("🚀 We Work Remotely Scraper (Updated Selectors)\n")

options = Options()
options.add_argument("--headless")

jobs = []

try:
    driver = webdriver.Firefox(options=options)
    driver.get("https://weworkremotely.com/remote-jobs/search?term=python")
    print("Page loaded...")
    time.sleep(6)

    # Updated selectors
    job_cards = driver.find_elements(By.TAG_NAME, "li")

    print(f"Total <li> elements found: {len(job_cards)}\n")

    for card in job_cards:
        try:
            title_element = card.find_element(By.CSS_SELECTOR, "span.title")
            title = title_element.text.strip()

            company_element = card.find_element(By.CSS_SELECTOR, "span.company")
            company = company_element.text.strip()

            location_element = card.find_elements(By.CSS_SELECTOR, "span.region")
            location = location_element[0].text.strip() if location_element else "Remote"

            link_element = card.find_element(By.TAG_NAME, "a")
            link = "https://weworkremotely.com" + link_element.get_attribute("href")

            if title and company and len(title) > 3:
                jobs.append({
                    'Job Title': title,
                    'Company': company,
                    'Location': location,
                    'Link': link,
                    'Scraped At': datetime.now().strftime("%Y-%m-%d %H:%M")
                })
        except:
            continue

except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()

# Save results
if jobs:
    df = pd.DataFrame(jobs)
    filename = f"python_jobs_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
    df.to_csv(filename, index=False)
    print(f"\n🎉 SUCCESS! {len(jobs)} jobs saved!")
    print(df)
else:
    print("\n❌ Still no jobs extracted.")
