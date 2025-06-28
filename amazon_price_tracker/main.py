import requests
from smtplib import SMTP
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

URL_AMAZON = ("https://www.amazon.ca/PlayStation-CFI-7019B01X-5-Pro-Console/dp/B0DGYL8TDZ/ref=sr_1_1"
    "?crid=26O333KT7GTPW&dib=eyJ2IjoiMSJ9.3oL9rJxRmyGzwbs6rePRM1E0Ks54ES12JojAw62L7bNxY7xSWGBhIKI7pgjy6"
    "_L3ICP0TtzhfkCxiNbzQc7Bh7NHC6Co1Kb2cErX3RN45iLC17796T6RPlLYLbY0DwH_uyENTqHPH9g-t--U-12_2R42LJSiQIr"
    "1KeAOE5Sj42qlBcd6ofXZH5k9fNYEBMCNUNkp-fLOi-pE2hLzizSs7l1k9rpXxYPJ2sxL7529ZfOSUbw59DaYtogcz7wXvRJsI"
    "qUtP3F9lgjFF_i7TZ0iFvWClU6ZQ4o-XN-vQmhNKHc.HasD44Kzzb0EjHjoYEiyCU4BjCfn9G6KW1EbQ0R4AEo&dib_tag=se&"
    "keywords=ps5%2Bpro%2Bconsole&qid=1750994072&sprefix=%2Caps%2C222&sr=8-1&th=1")
custom_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Ecoding": "gzip, deflate, br, zstd",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive"    
}


response = requests.get(URL_AMAZON, headers=custom_headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser") 

TARGET_PRICE = 850
current_price = float(soup.find(name="span", class_ = "aok-offscreen").get_text().replace("$",""))
print(current_price)
feedback = f"PlayStation 5 Pro Console is now ${current_price}\nVisit: {URL_AMAZON}"


if current_price <= TARGET_PRICE:
    with SMTP(os.environ["SMTP_ADDRESS"]) as connection:
        connection.starttls()
        connection.login(user=os.environ["EMAIL_ADDRESS"], password=os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject:Amazon Price Alert!!!\n{feedback}"
        )