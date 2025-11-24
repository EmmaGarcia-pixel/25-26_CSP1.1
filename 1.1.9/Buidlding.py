import turtle as trtl

painter = trtl.Turtle()

# Set base coordinates\pensize\speed
painter.penup()
painter.goto(-300,200)
painter.pensize(4)
painter.speed(500)
painter.pendown()

# change the color
wn = trtl.Screen()
wn.colormode(255)
r = 91
g = 11
b = 247
painter.pencolor(r,g,b)

shaded_lines = 100
length = 200

# Left wall
painter.right(25)

for shading in range(shaded_lines):
    painter.penup()
    painter.goto(painter.xcor(), painter.ycor()-int((length/shaded_lines)))
    painter.pendown()
    painter.forward(200)
    painter.backward(200)
    if g < 245:
        g += 10
    else:
        g = 11

# Right wall
painter.goto(-120, 115)
painter.left(50)

for shading in range(shaded_lines):
    painter.penup()
    painter.goto(painter.xcor(), painter.ycor()-int((length/shaded_lines)))
    painter.pendown()
    painter.forward(200)
    painter.backward(200)
    if g < 245:
        g += 10
    else:
        g = 11

# Roof 1st half
painter.goto(-300,200)

for shading in range(shaded_lines):
    painter.penup()
    painter.goto(painter.xcor(), painter.ycor()-int((length/shaded_lines)))
    painter.pendown()
    painter.forward(200)
    painter.backward(200)
    if g < 245:
        g += 10
    else:
        g = 11

 # Roof 2nd half
painter.goto(-120, 285)
painter.right(50)

for shading in range(shaded_lines):
    painter.penup()
    painter.goto(painter.xcor(), painter.ycor()-int((length/shaded_lines)))
    painter.pendown()
    painter.forward(200)
    painter.backward(200)
    if g < 245:
        g += 10
    else:
        g = 11

 # Left street
painter.goto(-300,0)

for shading in range(shaded_lines):
    painter.penup()
    painter.goto(painter.xcor(), painter.ycor()-int((length/shaded_lines)))
    painter.pendown()
    painter.forward(200)
    painter.backward(200)
    if g < 245:
        g += 10
    else:
        g = 11


wn = trtl.Screen()
wn.mainloop()
