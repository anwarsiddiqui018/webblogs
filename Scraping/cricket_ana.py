import csv      #to do operations on CSV
import pandas as pd  # file operations
from bs4 import BeautifulSoup as soup  #Scrapping tool
from urllib.request import urlopen as ureq # For requesting data from link
import numpy as np
import re

url = "http://howstat.com/cricket/Statistics/Players/PlayerList.asp?Group=A"
pagehtml = ureq(url)
soup = soup(pagehtml,"html.parser") #parse the html
table = soup.find("table", { "class" : "TableLined" })
with open('AZ.csv', 'a',newline='') as csvfile:
    f = csv.writer(csvfile)
for x in table:
    rows = table.find_all('tr') #find all tr tag(rows)
    for tr in rows:
        data=[]
        cols = tr.find_all('td') #find all td tags(columns)
        for td in cols:
            data.append(td.text.strip())
            print (data)



