"""

Write Python code to produce turtle graphics pattern as shown in the screen shot here:

*image of a hexagonal stop sign. Red fill with white text*

"""

import turtle
# Move the turtle into position and set the colour.
turtle.hideturtle() # We don't want the turtle visible.
turtle.penup()
turtle.setpos(-80, 140)
turtle.pendown()
turtle.color("Red")

# Now we can define the hexagon's values to ensure that all sides are even (and avoid magic numbers).
SIDES = 6
SIDE_LENGTH = 150
ANGLE = 60 # An even 60 degree angle for each turn (360 / no. of sides).

# Draw the hexagon and fill it in with red, using a for loop to draw each side with less code.
turtle.begin_fill()
for val in range(SIDES):
    turtle.forward(SIDE_LENGTH)
    turtle.right(ANGLE)
turtle.end_fill()

# Move the turtle and add the "STOP" text.
turtle.penup()
turtle.setpos(-85, -20)
turtle.pendown()
turtle.color("White")
turtle.write("STOP", font = ("Times New Roman", 48, "bold"))

turtle.done() # Called to ensure the graphic remains on screen.