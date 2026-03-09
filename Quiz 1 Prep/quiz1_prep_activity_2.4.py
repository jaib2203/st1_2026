""" 
ST1 Quiz 1 Prep - Activity 2.4

Write a program that prompts twice for an integer.
• The program should output the sum of the integers within the range of those two
numbers inclusively.
• For example, if the user inputs the numbers 10 and 15, then the sum would
be 75.
10 + 11 + 12 + 13 + 14 + 15 = 75
"""

int_1 = int(input("Enter an integer: "))
int_2 = int(input("Enter a second integer: "))

r = abs(int_2 - int_1) # Positive value regardless of which is bigger.
total = 0

# The smaller integer needs to be the starting value to count up. Check int_2 > int_1.
if int_2 > int_1:
    current_val = int_1
    for val in range(r + 1): # + 1 required for inclusivity.
        total += current_val
        current_val += 1
# Now check int_1 > int_2.
elif int_1 > int_2:
    current_val = int_2
    for val in range(r + 1):
        total += current_val
        current_val += 1

print(total)