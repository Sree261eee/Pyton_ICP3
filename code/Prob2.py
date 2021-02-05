import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Deep_learning'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.title.string)
rows = soup.find_all('a')
print(rows)
my_data_file = open('wikidata.txt', 'w')
for link in rows:
    filtered_data = link.get('href')
    print(filtered_data)
    my_data_file.write(str(filtered_data))
    my_data_file.write("\n")

my_data_file.close()