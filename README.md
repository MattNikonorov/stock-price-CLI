# Stock price CLI

Are you someone who can't help checking the latest stock prices every 5 minutes? Thanks to Python, getting the latest stock prices can be as easy as running `python3 main.py AMZN` in your terminal. In this tutorial, you will learn how to make a CLI with Python that:
1. Reads the ticker whose price you would like to get.
2. Scrapes the specified ticker's latest price.
3. Displays the scraped price.

***************
## Let's get started

First things first, create a new python file. For this tutorial, I'll name mine `main.py`. Once you have your new python file, import `sys`, `BeautifulSoup` and `requests`:
**main.py**
```
import sys
import requests
from bs4 import BeautifulSoup
```

Our CLI will need the user to input a ticker as a command-line argument after `python3 main.py`. Using the `sys` library, we can check if the user has entered a ticker and make the CLI return an error if no ticker was provided or if too many tickers were provided. This CLI will then define the `ticker` variable as the second argument provided by the user:
**main.py**
```
if len(sys.argv) > 2:
    print('You have specified too many tickers')
    sys.exit()

if len(sys.argv) < 2:
    print('No ticker provided')
    sys.exit()

ticker = sys.argv[1] # 0 = first argument and 1 = second argument
```

Now our CLI will need to scrape the provided ticker for it's latest price. We can do this using the `BeautifulSoup` and `requests` libraries.

The CLI will scrape the stock prices from [yahoo finance](https://finance.yahoo.com/). It will need to change the URL it scrapes based on the ticker entered by the user. Since the entered ticker gets stored inside the `ticker` variable, following yahoo finance's url structure, the CLI can change the `url` variable based on the ticker like so:
**main.py**
```
url = 'https://finance.yahoo.com/quote/' + ticker + '?p=' + ticker + '&.tsrc=fin-srch'
response = requests.get(url)
```
For example, if the provided ticker is `AMZN`, the CLI will scrape [this url](https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch).
If the provided ticker is instead `AAPL`, the CLI will scrape [this url](https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch).

**Full code:**
```
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
```

*************
### Scraping the stock price

For the actual scraping part, first go to a sample ticker's stock price webpage on yahoo finance. I'll choose [AMZN](https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch) for this tutorial. Locate the sample ticker's stock price element and right click on it. This will make a pop-up appear next to your cursor, click on the `inspect` option:
![Inspect the stock price](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/no469xj5l0vgnvo0hxcb.png)

This will make a large pop-up containing this webpage's DOM appear at the right of your screen with the selected stock price element highlighted in light blue:
![DOM pop-up](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/c2wp793xfv98bmgikf7m.png)

Select and copy the highlighted element's `class` property:
![Select class property](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/q6061qoxj9azpmw4x97g.png)

****************

Now that you have this element's `class` property, to scrape this ticker's latest stock price, add the following code to `main.py`:
**main.py**
```
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find('body').find(class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)')
    print('Latest stock price: ' + price.text.strip())
```
This code will find the stock price element through it's class property and display it's text contents using `price.text.strip()`.

**Full code:**
```
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

soup = BeautifulSoup(response.text, 'html.parser')
price = soup.find('body').find(class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)')
print('Latest stock price: ' + price.text.strip())
```

**One last thing!**
Put the last piece of code into a `try:` statement and return an error if the user entered an invalid ticker:
```
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
```

**********
## Time to test!

Now that you have the full code, it's time to run some tests.
**Check Amazon's stock price:**
![AMZN stock price](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/fn5cecuf6mjakq5yxn79.png)

**Check Apple's stock price:**
![AAPL stock price](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/bzbyyaxpol4unnfrlxxq.png)

**Input an invalid ticker:**
![Invalid ticker](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/d1agpi7n8snzxy8lbwy3.png)

*************

## Conclusion

I hope this article helped you learn about CLI development in Python, as well as gave you a fun and useful Python project idea.

