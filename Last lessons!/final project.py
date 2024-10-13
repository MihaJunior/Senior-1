import sqlite3
import requests
from bs4 import BeautifulSoup

def fetch_urls():
    connection = sqlite3.connect('FinalMyDB.sl3', 5)
    cursor = connection.cursor()
    cursor.execute('SELECT url FROM miha_sites')
    urls = cursor.fetchall()
    connection.close()
    return [url[0] for url in urls]

def search_text_in_url(url, text):
    response = requests.get(url+text)
    soup = BeautifulSoup(response.text, 'html.parser')
    ad_card_title_div = soup.find('div', {'data-cy': 'ad-card-title'})

    if ad_card_title_div:
        print(ad_card_title_div.get_text())
    else:
        print("Div with data-cy 'ad-card-title' not found.")

def main():
    urls = fetch_urls()
    search_text = input("Enter the text to search for: ")
    for url in urls:
        search_text_in_url(url, search_text)

if __name__ == "__main__":
    main()
