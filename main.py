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


def send_email():
    """Dummy function! Will be updated later with email sending
    functionality"""
    print("Email was sent!")


def store(extracted):
    """Store extracted data into a text file."""
    with open("data.txt", "a") as file:
        file.write(extracted + "\n")


def read():
    """Read and return the content from the data.txt file."""
    with open("data.txt", "r") as file:
        return file.read()


# Scrape the website and extract tour information
scraped = scrape(URL)
extracted = extract(scraped)
content = read()

# Check for new upcoming tours, store and send an email if found
if extracted.lower() != "no upcoming tours":
    if extracted not in content:
        store(extracted)
        send_email()
