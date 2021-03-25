
import bs4  # beautiful soup helps us parse HTML on websites.
import requests

res = requests.get("https://www.marketwatch.com/investing/future/sp%20500%20futures")
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'html.parser') #we pass the string with the html, and this gets us a soup object.
#we put in the 'html.parser' second argument to avoid the warning.

elems_Market_Price = soup.select('body > div.container.container--body > div.region.region--intraday > \
div.column.column--aside > div > div.intraday__data > h3 > bg-quote') #We select the part of the HTML 

# document that we want using the CSS selector path. (Right click, copy--> copy selector)
elems_Change_In_Price = soup.select('body > div.container.container--body > div.region.region--intraday > \
div.column.column--aside > div > div.intraday__data > bg-quote > span.change--point--q')
elems_Change_In_Price_Percent = soup.select('body > div.container.container--body > div.region.region--intraday \
> div.column.column--aside > div > div.intraday__data > bg-quote > span.change--percent--q')

print('Current Market Price (15min delay) is:', elems_Market_Price[0].text.strip()) #This gets the price!

if float(elems_Change_In_Price[0].text.strip()) > 0:
    print('Day/Day Change in Price is: +{}'.format(elems_Change_In_Price[0].text.strip()), \
    '(+{})'.format(elems_Change_In_Price_Percent[0].text.strip()))
else:
    print('Day/Day Change in Price is:', elems_Change_In_Price[0].text.strip(), \
    '({})'.format(elems_Change_In_Price_Percent[0].text.strip()))

