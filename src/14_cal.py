"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 [X] If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

def program():
  userInput = input("File name month year:")
  inputList = userInput.split(" ")

  if len(inputList) > 3:
    print("Incorrect form, input should be [file] [month] [year]")
    return


  if userInput == "":
    m = datetime.today().month
    y = datetime.today().year
    print(calendar.month(y, m=m))
    return

  if len(inputList) > 1:
    m = inputList[1]
  else:
    m = datetime.today().month
  
  if len(inputList) > 2:
    y = inputList[2]
  else:
    y = datetime.today().year
  print(m, y)
  print(calendar.calendar(int(y), int(m)))  

  
program()
