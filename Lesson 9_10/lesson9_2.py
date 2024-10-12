from locale import currency

import requests

response = requests.get('https://coinmarketcap.com/')

response_parce = response.text.split("<span>")

cur = 0

found = False
for page in response_parce:
    if page.startswith("$"):
        for page1 in page.split("</span"):
            if page1.startswith("$") and page1[1].isdigit():
                cur = page1
                found = True
                break
        if found:
            break

amount_float = float(cur.replace(",", "").replace("$", ""))


while True:
    user_input = input(f"Курс валюти біткоїна - {amount_float}. Введіть кількість біткоїнів: ")
    try:
        number = float(user_input)
        result = number * amount_float
        print(f"Ваш прибуток: {result} доларів")
    except ValueError:
        print("Будь ласка, введіть коректне число.")
