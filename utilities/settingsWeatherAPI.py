import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utilities.randomCity import capital_city


with open('../utilities/api_key.txt', 'r') as file:
    API_KEY = file.read().strip()
se = requests.session()
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
CITY = capital_city
url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY


def buildURL(api_key, tc_city):
    return BASE_URL + "appid=" + api_key + "&q=" + tc_city


def responseGet(api_key, tc_city, sc):
    request_url = buildURL(api_key, tc_city)
    response = se.get(request_url, params={'AuthorName:': "Victor Bizzi Melo"})
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")
    assert response.status_code == sc
    return response


def validateCapitalName(response):
    city_response_name = response.json()['name']
    assert capital_city == city_response_name





