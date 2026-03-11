"""

Write Python code to produce turtle graphics pattern as shown in the screen shot here:

*image of the Olympic rings*

"""

import turtle
turtle.hideturtle() # We don't want the turtle visible.
turtle.pensize(8) # Make the rings thicker.

# First (blue) ring. 
# Move the turtle into position, raising and lowering the pen to avoid lines between positions.
turtle.penup()
turtle.setpos(-150, 50)
turtle.pendown()
# Draw a blue circle.
turtle.color("Blue")
turtle.circle(60)


# Second (black) ring. 
# Move the turtle into position.
turtle.penup()
turtle.setpos(0, 50)
turtle.pendown()
# Draw a black circle.
turtle.color("Black")
turtle.circle(60)

# Third (red) ring. 
# Move the turtle into position.
turtle.penup()
turtle.setpos(150, 50)
turtle.pendown()
# Draw a red circle.
turtle.color("Red")
turtle.circle(60)

# Fourth (yellow) ring. 
# Move the turtle into position.
turtle.penup()
turtle.setpos(-75, -10)
turtle.pendown()
# Draw a yellow circle.
turtle.color("Yellow")
turtle.circle(60)

# Fifth (green) ring. 
# Move the turtle into position.
turtle.penup()
turtle.setpos(75, -10)
turtle.pendown()
# Draw a green circle.
turtle.color("Green")
turtle.circle(60)

turtle.done() # Called to ensure the graphic remains on screen.