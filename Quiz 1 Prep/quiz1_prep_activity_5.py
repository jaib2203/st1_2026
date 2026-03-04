# ST1 Quiz 1 Prep - Activity 5

# Write an application that prompts to enter the radius of a circle.
# Accept the user input into a variable.
# Compute and print the area of the circle whose radius was input.
# The formula for the area of a circle is πr² (pi times the square of the radius).
# Use 3.14159 for pi.

r = float(input("Enter the radius of a circle: "))
PI = 3.14159

print(f"The area of your circle is {(PI * r ** 2):.2f}")