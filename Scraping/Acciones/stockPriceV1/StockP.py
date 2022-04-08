import bs4
import requests
from bs4 import BeautifulSoup

r = requests.get('https://finance.yahoo.com/quote/FB?p=FB')
soup = bs4.BeautifulSoup(r.text,"xml")
#price = soup.find_all('div',{'class':'D(ib) Mend(20px)'})[0].find('fin-streamer').text 

print(soup)
#print(price)

