import requests
from bs4 import BeautifulSoup  #Scrapping tool
import pandas as pd

URL = "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2019;trophy=117;type=season"
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)

columns = ['Team 1', 'Team 2', 'Winner', 'Margin',  'Ground', 'Match Date', 'Scorecard']
df = pd.DataFrame(columns=columns)

table = soup.find('table', attrs={'class': 'engineTable'}).tbody
# print(table)
trs = table.find_all('tr')
for tr in trs:
    tds = tr.find_all('td')
    row = [td.text.replace('\n', '') for td in tds]
    df = df.append(pd.Series(row, index=columns), ignore_index=True)

df.to_csv('ipl_2019.csv', index=False)

