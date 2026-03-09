""" 
ST1 Quiz 1 Prep - Activity 2.6

Ask the user to input three numbers representing a lower limit, a higher limit, and a step
value.
• The program should use a range object to loop through and print the numbers
from low to high (inclusive), taking into consideration the step.
"""

low_limit = int(input("Enter an integer representing a lower limit: "))
high_limit = int(input("Enter an integer representing an upper limit: "))
step_val = int(input("Enter an integer representing a step value: "))

r = abs(high_limit - low_limit)

for num in range(r + 1):
    if low_limit > high_limit:
        break
    print(low_limit)
    low_limit += step_val