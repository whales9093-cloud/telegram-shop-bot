from selenium import webdriver
from selenium.webdriver.firefox.options import Options

print("🧪 Testing Firefox + Selenium...\n")

options = Options()
options.add_argument("--headless")

try:
    driver = webdriver.Firefox(options=options)
    driver.get("https://google.com")
    print("✅ SUCCESS! Selenium with Firefox is working!")
    print("Page Title:", driver.title)
    driver.quit()
except Exception as e:
    print("❌ Error:", str(e))
