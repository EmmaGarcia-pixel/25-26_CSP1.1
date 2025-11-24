import turtle as trtl

painter = trtl.Turtle()

painter.penup()
painter.forward(-100)
painter.pendown()
painter.circle(50)
painter.circle(30)
painter.penup()
painter.forward(200)
painter.pendown()
painter.circle(50)
painter.circle(30)
painter.penup()
painter.backward(200)
painter.pendown()


wn = trtl.Screen()
wn.mainloop()