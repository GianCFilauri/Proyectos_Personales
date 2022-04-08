from email import header
from pickle import TRUE
from pyppeteer import executablePath
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"}
url = 'https://www.instagram.com/420madisonivy/'
response = requests.get(url, headers = header)
soup = BeautifulSoup(response.text, 'html.parser')
soup.find_all('a')
print(soup)

#DRIVER_PATH = 'C:/path/chromedriver'
#driver = webdriver.Chrome(executable_path = DRIVER_PATH)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver.get("https://www.google.com")
driver.get('https://www.instagram.com/420madisonivy/')
driver.page_source

soup2 = BeautifulSoup(driver.page_source, "html.parser")

image_link = []
for a in soup.find_all('a', href=True):
    if a['href'].startswith('/p'):
        image_link.append("https://www.instagram.com"+a['href'])
        print("Found the URL:", "https://www.instagram.com"+a['href'])
