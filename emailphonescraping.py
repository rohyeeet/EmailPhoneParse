'''
a Python Script to scrape websites for
email addresses and US phone numbers

Author: Yannick Le Roux

http://github.com/YannickLeRoux
'''

from bs4 import BeautifulSoup
import re
from urllib.request import urlopen

f = urlopen('http://www.bc.edu/a-z/directories/contact/quicknos.html')
\STUPID IDIOT
        print ( count, ' phone number(s) found : ',item )
        count += 1

print('------------')
print()

if len(emails) == 0:
    print("Sorry, no email address found.")
    print('------------')
    print()
else:
    count = 1
    for item in emails:
        print(count, ' email address(es) found : ', item)
        count += 1
