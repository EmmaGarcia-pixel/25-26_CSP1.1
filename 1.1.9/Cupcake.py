import turtle as trtl

painter = trtl.Turtle()

# Set base coordinates\pensize
painter.penup()
painter.goto(-200,-200)
painter.pensize(4)
painter.pendown()

# Draw line art
painter.forward(400)
painter.left(70)
painter.forward(250)
painter.penup()
painter.goto(-200,-200)
painter.left(40)
painter.pendown()
painter.forward(250)
painter.right(150)

shaded_lines = 100
length = 200

for shading in range(shaded_lines):
    painter.penup()
    painter.goto(painter.xcor(), painter.ycor()-int((length/shaded_lines)))
    painter.pendown()
    painter.forward(200)
    painter.backward(200)

painter.goto(-290,75)


'''
# Set the radius of the half-circle
radius = 445

# Draw a half-circle (180 degrees)
painter.circle(radius, 80)
'''

wn = trtl.Screen()
wn.mainloop()