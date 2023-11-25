import time
import requests
import selectorlib
import smtplib
import ssl
import os
from dotenv import load_dotenv

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


def send_email(message):
    """Send an email indicating new upcoming tour."""
    # Gmail SMTP server details
    host = "smtp.gmail.com"
    port = 465

    # Load email and app password from environmental variables
    load_dotenv()
    sender_email = os.getenv("EMAIL")
    receiver_email = os.getenv("EMAIL")
    app_password = os.getenv("PASSWORD")

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Convert the message to bytes using UTF-8 encoding
    message = message.encode('utf-8')

    # Connect to the SMTP server and send the email
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        # Login to the sender's Gmail account
        server.login(sender_email, app_password)

        # Send the email from the sender to the receiver
        server.sendmail(sender_email, receiver_email, message)


def store(extracted):
    """Store extracted data into a text file."""
    with open("data.txt", "a") as file:
        file.write(extracted + "\n")


def read():
    """Read and return the content from the data.txt file."""
    with open("data.txt", "r") as file:
        return file.read()


while True:
    # Scrape the website and extract tour information
    scraped = scrape(URL)
    extracted = extract(scraped)
    content = read()

    # Check for new upcoming tours, store and send an email if found
    if extracted.lower() != "no upcoming tours":
        if extracted not in content:
            store(extracted)
            send_email(message="Subject: New Event!" +
                               "\n" +
                               "Hey, a new event has been found!" +
                               "\n" +
                               f"{extracted}")
    time.sleep(2)