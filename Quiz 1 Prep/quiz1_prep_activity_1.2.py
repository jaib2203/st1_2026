# ST1 Quiz 1 Prep - Activity 2

# Write a program that prompts twice for text from the user.
# The ﬁrst input should be a ﬁrst name.
# The second input should be a last name.
# The program should print the full name on one line and the person's initials on the second line.

f_name = input("Please enter a first name: ")
l_name = input("Please enter a last name: ")
print(f"Full name: {f_name} {l_name} \nInitials: {f_name[0]}{l_name[0]}")