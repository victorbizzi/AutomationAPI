import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '')))
from utilities.settingsWeatherAPI import *

#
@pytest.mark.weatherAPI
def test_getValidCityWeather():
    response = responseGet(API_KEY, CITY, 200)
    validateCapitalName(response)


@pytest.mark.weatherAPI
def test_getInvalidCityWeather():
    city = "Tchurubatu"
    responseGet(API_KEY, city, 404)


@pytest.mark.weatherAPI
def test_getWithoutAPIKey():
    responseGet('', CITY, 401)


@pytest.mark.weatherAPI
def test_getInvalidAPIKey():
    apikey_test = "84yty3h487ghw8y4hbgfyw"
    responseGet(apikey_test, CITY, 401)
