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
    while True:
        try:
            userInput = input("Please enter the month (1-12), then the year:")
        
            inputList = userInput.split(" ")

            m = int(inputList[0])
            m = int(m)
            
            y = inputList[1]
            y = int(y)
            break
        #For arguments not being integers
        except ValueError as err:
            #If no arguments are entered
            if m == "":
                m = datetime.today().month           
                y = datetime.today().year
                break
            else:
                print("Month's need to be as a number")

        except IndexError as err:
            #M is always available, sometime empty, so this is incase y is not
            y = datetime.today().year
            break
        #In case of any errors I can't think of
        except:
            print("Incorrect form, input should be [month (1-12)] [year]. For example: '1 2019'")
        
    print(calendar.month(y, m))




program()


#Value Error: "May etc"
#Index Error: "Only one month"