import requests
import smtplib
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

URL = "https://appbrewery.github.io/instant_pot/"
TARGET_PRICE = 100

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

price = float(soup.find(class_="a-offscreen").getText().split("$")[1])
title = soup.find(id="productTitle").getText().strip()

if price < TARGET_PRICE:
    message = f"""
    Subject:Amazon Price Alert!

    {title}
    is now ${price}

    Buy now:
    {URL}
    """

    with smtplib.SMTP(os.getenv("SMTP_ADDRESS"), 587) as connection:
        connection.starttls()
        connection.login(
            os.getenv("EMAIL_ADDRESS"),
            os.getenv("EMAIL_PASSWORD")
        )
        connection.sendmail(
            os.getenv("EMAIL_ADDRESS"),
            os.getenv("EMAIL_ADDRESS"),
            message
        )
