import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.worldometers.info/coronavirus/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', {'id': 'main_table_countries_today'})
rows = table.find_all('tr', {'class': ['total_row_world', 'even', 'odd']})[:10]

data = []
for row in rows:
    cells = row.find_all('td')

    country = cells[1].text.strip()
    total_cases = cells[2].text.strip()
    total_deaths = cells[4].text.strip()
    total_recovered = cells[6].text.strip()

    data.append({
        'Country': country,
        'Total Cases': total_cases,
        'Total Deaths': total_deaths,
        'Total Recovered': total_recovered,
    })

with open('covid_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Country', 'Total Cases', 'Total Deaths', 'Total Recovered']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow(row)
