import turtle as trtl

painter = trtl.Turtle()

# Set base coordinates\pensize\speed
painter.penup()
painter.pensize(4)
painter.speed(500000)
painter.pendown()

shaded_lines = 300
length = 600

# Change the color
wn = trtl.Screen()
wn.colormode(255)
r = 107
g = 205
b = 227
painter.pencolor(r,g,b)

#---------- Sky -------------

# Base color
painter.goto(-500,400)

for shading in range(shaded_lines):
    painter.penup()
    painter.goto(painter.xcor(), painter.ycor()-int((length/shaded_lines)))
    painter.pendown()
    painter.forward(1000)
    painter.backward(1000)
    if g < 245:
        g += 10
    else:
        g = 11

#---------- Building 1 ------------

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
painter.goto(-300,200)
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

'''

 # Roof 2nd half
painter.penup()

'''

painter.goto(-120, 285)
painter.right(50)

'''

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

#---------- Street -------------

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

'''

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

shaded_lines -= 50
length -= 50

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
        
'''

# Right street
painter.penup()
painter.goto(-120, -85)
painter.left(50)
painter.pendown()

for shading in range(shaded_lines):
    painter.penup()
    painter.goto(painter.xcor(), painter.ycor()-int((length/shaded_lines)))
    painter.pendown()
    painter.forward(4200)
    painter.backward(4200)
    if g < 245:
        g += 10
    else:
        g = 11

# Change the color
wn = trtl.Screen()
wn.colormode(255)
r = 150
g = 150
b = 150
painter.pencolor(r,g,b)

# Right sidewalk
painter.penup()
painter.goto(-120, -285)
painter.pendown()

for shading in range(shaded_lines):
    painter.penup()
    painter.goto(painter.xcor(), painter.ycor()-int((length/shaded_lines)))
    painter.pendown()
    painter.forward(4200)
    painter.backward(4200)
    if g < 245:
        g += 10
    else:
        g = 11

# Left sidewalk
painter.penup()
painter.goto(-500,-110)
painter.right(50)
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
