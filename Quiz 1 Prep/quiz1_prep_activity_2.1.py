""" 
ST1 Quiz 1 Prep - Activity 2.1

Write a program that prompts for a lucky number. The program should print out a
message if the number entered is not an integer.
"""

num = input("Please enter a lucky number: ")
index = num.find(".")
if index == -1:
    print("Number is an integer")
else:
    print("Number is a float")