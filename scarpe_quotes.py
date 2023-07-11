import os
from click import OptionParser, option
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option(
    "prefs", {"profile.managed_default_content_settings.images": 2}
)

chrome_driver_path = r'C:\Users\admin\OneDrive\Desktop\selenium\chromedriver_win32\chromedriver.exe'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get("http://quotes.toscrape.com")



page = 0
while True:
    for i in range(1, 11):
        quote_xpath = f"/html/body/div[1]/div[2]/div[1]/div[{i}]/span[1]"
        author_xpath = f"/html/body/div[1]/div[2]/div[1]/div[{i}]/span[2]/small"

        quote_element = driver.find_element(By.XPATH, quote_xpath)
        quote_text = quote_element.text
        author_element = driver.find_element(By.XPATH, author_xpath)
        author_name = author_element.text

        print("Quote:", quote_text)
        print("Author:", author_name)
        print()

        document = {
            'quote_id': page * 10 + i,
            'quote': quote_text,
            'author': author_name
        }

    try:
        next_button = driver.find_element(By.XPATH, "//li[@class='next']/a")
        next_button.click()
        page += 1
    except:
        print("No more pages available. Exiting loop.")
        break

driver.quit()
