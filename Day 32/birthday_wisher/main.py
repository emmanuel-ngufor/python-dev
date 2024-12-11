from datetime import datetime
import pandas as pd
import random
import smtplib
from creds import EMAIL, PASSWORD


today_tuple = (datetime.now().month, datetime.now().day)
data = pd.read_csv("birthdays.csv")
birthdays_dict = {(row.month, row["day"]): row for (index, row) in data.iterrows()}

if (today_tuple) in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL, 
            to_addrs=birthday_person["email"], 
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )   