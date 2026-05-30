import requests
from bs4 import BeautifulSoup
import time

print("🔥 Simple Web Scraper Starting...\n")

url = "https://quotes.toscrape.com/"

try:
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    
    print(f"✅ Successfully scraped {len(quotes)} quotes!\n")
    
    for i in range(min(5, len(quotes))):
        quote = quotes[i].text
        author = authors[i].text
        print(f"{i+1}. {quote}")
        print(f"   — {author}\n")
        time.sleep(0.5)

except Exception as e:
    print(f"❌ Error: {e}")
