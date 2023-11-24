import requests
import selectorlib

URL = "https://programmer100.pythonanywhere.com/tours/"


def scrape(url):
    """Scrape the page source from URL"""
    response = requests.get(url)
    source = response.text
    return source


print(scrape(URL))