import datetime as dt
import random
import smtplib

from dotenv import load_dotenv
import os

# Good way to have all configuartions done and should be call before everything else
def configure():
    load_dotenv()

# Configure settings for sensitave data
configure()


# Get day of week using datetime lib
now = dt.datetime.now()
day_of_week = now.weekday()

# Read quotes.txt and get a list of quotes
if day_of_week == 2:
    with open(file="quotes.txt", mode="r") as quote_file:
        all_quotes = quote_file.readlines()
        # Get a random quotes from the list
        quote = random.choice(all_quotes)



    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=os.getenv("MY_EMAIL"), password=os.getenv("MY_PASSWORD"))
        connection.sendmail(
            from_addr=os.getenv("MY_EMAIL"), 
            to_addrs=os.getenv("MY_EMAIL"), 
            msg=f"Subject:Motivational Quote\n\n{quote}"
        )                                                                                                                                   