# ST1 Quiz 1 Prep - Activity 3

# Write a program that accepts a string from the user.
# Determine and print the following information about the string:
# Does it end in a period?
# Does it contain all alphabetic characters?
# Is there an 'x' in the string?
# Create and print a new string that has all occurrences of e changed to E.

string = input("Please enter a string: ")

# Does it end in a period?
if string[-1] ==".":
    print("String ends in a period.")
else:
    print("String does not end in a period.")

# Does it contain all alphabetic characters?
if string.isalpha():
    print("String is entirely alphabetic.")
else:
    print("String includes non-alphabetic characters.")

# Is there an 'x' in the string?
if "x" in string:
    print("There is an 'x' in the string.")
else:
    print("There is NO 'x' in the string.")

# Create and print a new string that has all occurrences of e changed to E.
print(f"Here is your string with capitalised Es: {string.replace("e", "E")}")