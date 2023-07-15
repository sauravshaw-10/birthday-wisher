##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import random
import pandas

now = dt.datetime.now()
day = now.day
month = now.month

data = pandas.read_csv("birthdays.csv")
birth_month = data[data["month"] == month]
birth_day = data[data["day"] == day]

MY_EMAIL = "saurav.shaw10@gmail.com"
MY_PASSWORD = "qwxuglkmnyysjbgp"

PLACEHOLDER = "[NAME]"
random_chance = random.randint(1,3)


def letter(chance):
    if int(birth_day.day) == day and int(birth_month.month) == month:

        with open(f"./letter_templates/letter_{chance}.txt") as email:
            content = email.read()
            name = data.loc[birth_day.index, "name"]
            l_name = name.to_list()
            birthday_mail = content.replace(PLACEHOLDER, l_name[0])

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="sshaw@me.iitr.ac.in",
                                msg=f"Subject: Happy Birthday!\n\n{birthday_mail}"
                                )


letter(random_chance)















