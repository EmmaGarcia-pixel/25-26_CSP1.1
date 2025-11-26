import turtle as trtl

painter = trtl.Turtle()

# Set base coordinates\pensize\speed
painter.penup()
painter.goto(-300,200)
painter.pensize(4)
painter.speed(500)
painter.pendown()

shaded_lines = 100
length = 200

# Change the color
wn = trtl.Screen()
wn.colormode(255)
r = 173
g = 89
b = 80
painter.pencolor(r,g,b)

# Left wall
painter.penup()
painter.right(25)
painter.pendown()

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

'''

# Change the color
wn = trtl.Screen()
wn.colormode(255)
r = 168
g = 82
b = 72
painter.pencolor(r,g,b)

# Right wall
painter.penup()
painter.goto(-120, 115)
painter.left(50)
painter.pendown()

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

# Change the color
wn = trtl.Screen()
wn.colormode(255)
r = 204
g = 94
b = 82
painter.pencolor(r,g,b)

# Roof 1st half
painter.penup()
painter.goto(-300,200)
painter.pendown()

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
painter.penup()
painter.goto(-120, 285)
painter.right(50)
painter.pendown()

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

'''

# Change color
wn = trtl.Screen()
wn.colormode(255)
r = 0
g = 0
b = 0
painter.pencolor(r,g,b)

 # Left street
painter.penup()
painter.goto(-500,92)
painter.pendown()

for shading in range(shaded_lines):
    painter.penup()
    painter.goto(painter.xcor(), painter.ycor()-int((length/shaded_lines)))
    painter.pendown()
    painter.forward(420)
    painter.backward(420)
    if g < 245:
        g += 10
    else:
        g = 11

# Change color
wn = trtl.Screen()
wn.colormode(255)
r = 255
g = 217
b = 0
painter.pencolor(r, g, b)

# Left street yellow line things
painter.penup()
painter.goto(-400,0)
painter.pendown()

for shading in range(shaded_lines):
    painter.penup()
    painter.goto(painter.xcor(), painter.ycor()-int((length/shaded_lines)))
    painter.pendown()
    painter.forward(10)
    painter.backward(10)
    if g < 245:
        g += 10
    else:
        g = 11

# Right street
painter.penup()
painter.goto(-120, -85)
painter.left(50)
painter.pendown()

for shading in range(shaded_lines):
    painter.penup()
    painter.goto(painter.xcor(), painter.ycor()-int((length/shaded_lines)))
    painter.pendown()
    painter.forward(420)
    painter.backward(420)
    if g < 245:
        g += 10
    else:
        g = 11



wn = trtl.Screen()
wn.mainloop()
