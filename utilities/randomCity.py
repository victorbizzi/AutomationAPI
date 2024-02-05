import requests
import random


def get_random_capital_city():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)

    if response.ok:
        countries = response.json()
        random_country = random.choice(countries)
        capital = random_country.get('capital', ['None found'])[0]
        return capital
    else:
        return "Failed!"


capital_city = get_random_capital_city()
print(f"Random capital city: {capital_city}")
