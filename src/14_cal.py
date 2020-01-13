"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 NONE => current month
 - one arg => curren month
 - month and year
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime


def program():
    userInput = input("Please enter the month, then the year:")
    inputList = userInput.split(" ")

    if len(inputList) > 2:
        print("Incorrect form, input should be [month] [year]")
        return

    if userInput == "":
        m = datetime.today().month
        y = datetime.today().year

    if len(inputList) == 1:
        m = inputList[0]
        y = datetime.today().year

    if len(inputList) == 2:
        m = inputList[0]
        y = inputList[1]

    print(calendar.month(int(y), int(m)))


program()
