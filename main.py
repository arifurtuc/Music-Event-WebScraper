import requests
import selectorlib

URL = "https://programmer100.pythonanywhere.com/tours/"


def scrape(url):
    """Scrape the page source from URL."""
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    """Extract relevant data using a SelectorLib extractor configuration."""
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


scraped = scrape(URL)
extracted = extract(scraped)
print(extracted)