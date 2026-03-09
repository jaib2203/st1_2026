""" 
ST1 Quiz 1 Prep - Activity 2.5

Ask the user to input multiple numbers on one input line.

• Split the numbers into a list.
• Write a loop that examines each element of the list and displays the ones that
are greater than zero.
"""

nums = input("Please input multiple numbers with spaces in between: ")
nums_list = nums.split(" ")

for num in nums_list:
    if float(num) > 0:
        print(num)