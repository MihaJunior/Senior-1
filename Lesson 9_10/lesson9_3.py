from bs4 import BeautifulSoup
import requests

response = requests.get('https:// coinmarketcap.com/')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    soup_list = soup.find_all('div', class_='sc-b3fc6b7-0 dzgUIj')
    for element in soup_list:
        print(element.text)


