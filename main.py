##################### Normal Starting Project ######################
import datetime as dt
import smtplib
import pandas
import random
allLetters = ["letter_1.txt","letter_2.txt","letter_3.txt"]

myEmail = "YOUR EMAIL HERE"
password = "YOUR PASSWORD HERE"

today = (dt.datetime.today().month,dt.datetime.today().day)
data = pandas.read_csv("birthdays.csv")
birtdaysDict = {(row.month,row.day):row for (index,row) in data.iterrows()}
if today in birtdaysDict:
    randomLetter = random.choice(allLetters)
    with open(f"letter_templates/{randomLetter}") as letters:
        letter = letters.read()
        newLetter = letter.replace("[NAME]", f"{birtdaysDict[today][0]}")
        print(newLetter)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=myEmail,password=password)
        connection.sendmail(from_addr=myEmail,to_addrs=birtdaysDict[today][1],msg=f"Subject:Happy Birthday!\n\n{newLetter}".encode("utf-8"))




