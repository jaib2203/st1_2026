""" 
ST1 Quiz 1 Prep - Activity 2.2

Rewrite the preceding exercise to additionally print out how many digits are in the
number, if the number is an integer.
"""

num = input("Please enter a lucky number: ")
index = num.find(".")
if index == -1:
    print("Number is an integer")
    digits = len(num)
    print(f"There are {digits} digits.")
else:
    print("Number is a float")