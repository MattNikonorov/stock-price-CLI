import os
import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv) > 2:
    print('You have specified too many tickers')
    sys.exit()

if len(sys.argv) < 2:
    print('No ticker provided')
    sys.exit()

ticker = sys.argv[1]

url = 'https://finance.yahoo.com/quote/' + ticker + '?p=' + ticker + '&.tsrc=fin-srch'
response = requests.get(url)
try:
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find('body').find(class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)')
    print('Latest stock price: ' + price.text.strip())
except:
    print('Invalid ticker')
