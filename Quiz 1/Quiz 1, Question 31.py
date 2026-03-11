"""

One pound weight is equivalent to 0.454 kilograms.

Write a Python program (Console Program/Not GUI program) that
asks the user to enter the weight of an object in pounds and then
calculates and displays the weight of the object in kilograms.

"""

# First we require the user input (as a float).
weight_lb = float(input("Enter an object's weight in pounds: "))

# Then we need to convert the input from lbs to kgs.
weight_kg = weight_lb * 0.454

# Output the weight in kilograms.
print(f"The object's weight in kilograms is: {weight_kg:.2f}")