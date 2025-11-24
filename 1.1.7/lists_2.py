#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["turtle", "circle", "square", "triangle", "classic", "circle", "square", "triangle"]
for shape in turtle_shapes:
    turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "pink", "teal"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.color(turtle_colors.pop())
  t.penup()
  my_turtles.append(t)

# Determines starting coordinates
startx = 0
starty = 0
direction = 90

# Moves turtle position
for t in my_turtles:
  t.goto(startx, starty)
  t.setheading(direction)
  t.setheading(direction)
  t.right(45)
  t.forward(50)
  t.pendown()

#
  startx = t.xcor()
  starty = t.ycor()
  direction = t.heading()

wn = trtl.Screen()
wn.mainloop()

