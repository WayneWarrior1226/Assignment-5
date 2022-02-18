#This code was created by Veronica Dean on 2/17/2022

import math

#Get inputs from user
firstname = input("Please enter your first name: ")
lastname = input("Please enter your last name: ")


#convert names into propper letters
firstname=firstname.upper()
lastname=lastname.lower()

#output to user
print("Hello,",firstname,lastname,"\n","\n")

#convert first and last name into one name
name = firstname + ' ' + lastname
print(name)

#split the strings back up
name1,name2 = name.split(' ')

#output the new value
print(name2,'Walsh College Student')

#output a quote to user
print('"Start by doing what\'s necessary: then do what\'s possible: and suddenly you are doing the impossible - Francis of Assisi"')

#stores two decimal numbers as variables
num1 = float(1.5)
num2 = float(2.4)

#stores numeric values after operations
added = (num1 + num2) 
subtracted = (num1 - num2) 
multiplied = (num1 * num2)
divided = (num1/num2)

#declare variables to print in a variety of ways
plus = ' plus '
eq = ' equals '

#outputs numbers to user in different ways
print(num1,plus,num2,eq,added)
print(num1,' minus ', num2 ,' equals ',subtracted)
print(num1,' multiplied by ',num2, ' equals ',num1*num2)
print(f"{num1} divided by {num2} equals {divided}")

#declare square root variable
sq_root = format(math.sqrt(multiplied), '.2f')

#output the square root variable
print("The square root of ",multiplied," equals ",sq_root)

#gather the current date/time
from datetime import datetime
now = datetime.now()
day = datetime.now().day
month = now.strftime('%B')

#output the day and month
print("\n\t\tToday is day", day, "of the month of", month,".")



