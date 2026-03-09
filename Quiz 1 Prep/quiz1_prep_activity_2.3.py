""" 
ST1 Quiz 1 Prep - Activity 2.3

Write a program that prompts twice for an integer.
• The program should print the larger of the two numbers.
• If the numbers are equal, then the program should indicate it as such.
"""

int_1 = int(input("Enter an integer: "))
int_2 = int(input("Enter a second integer: "))

if int_1 > int_2:
    print(f"{int_1} is the bigger number.")
elif int_1 == int_2:
    print("The numbers are equal.")
else:
    print(f"{int_2} is the bigger number.")