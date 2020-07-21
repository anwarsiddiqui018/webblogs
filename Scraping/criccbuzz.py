import requests
from bs4 import BeautifulSoup #Scrapping tool
import pandas as pd

URL = "https://www.cricbuzz.com/cricket-team/india/2/stats"
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)

columns = ['Player', 'Matches', 'Inns', 'Runs',  'Avg', 'Sr', '4S', '6S']
df = pd.DataFrame(columns=columns)

table = soup.find('table', attrs={'class': 'table table-responsive cb-series-stats'}).tbody
# print(table)
trs = table.find_all('tr')
for tr in trs:
    tds = tr.find_all('td')
    row = [td.text.replace('\n', '') for td in tds]
    df = df.append(pd.Series(row, index=columns), ignore_index=True)

df.to_csv('indian player stats.csv', index=False)