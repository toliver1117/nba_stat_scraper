from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.basketball-reference.com/leagues/NBA_2024.html')
nba_web_page = response.text


soup = BeautifulSoup(nba_web_page, 'html.parser')

data = []
table = soup.find('table', attrs={'id': 'per_game-team'})
table_body = table.find('tbody')

for t in table_body.find_all('tr'):
    print(t.getText())


