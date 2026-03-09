# ST1 Quiz 1 Prep - Activity 8

# Write a program that prompts the user twice for a number.
# The ﬁrst number will be the base, and the second number will be the exponent. 
# Print the result of raising the base to the exponent.

base = int(input("Enter a number: "))
exp = int(input("Enter an second number: "))

print(f"{base} raised to the power of {exp} = {base ** exp}")