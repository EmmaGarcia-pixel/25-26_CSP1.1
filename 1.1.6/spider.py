# CODE TO ADD
#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less use
# ful variable name x is used
spider = trtl.Turtle()

# create spider body
spider.pensize(40)
spider.circle(20)

# create spider head
spider.penup()
spider.goto(0,40)
spider.pendown()
spider.pensize(30)
spider.circle(15)

# create spider eyes
'''
spider.penup()
spider.goto(-20,40)
spider.pendown()
spider.pensize(10)
spider.circle(20)
'''

# configure spider legs
num_of_legs = 8
length_of_legs = 50
#length_of_legs = 70
angle = 360 / num_of_legs - 25
spider.pensize(5)

# draw legs
'''
while (heading < num_of_legs):
  spider.goto(0,20)
  spider.setheading(direction_of_legs * heading)
  spider.forward(length_of_legs)
  heading = heading + 1
'''

leg = 0
radius = 60
while (leg < num_of_legs):
  spider.goto(0,20)
  if leg < 4:
      spider.setheading(angle*leg + 125)
      spider.pendown()
      spider.circle(radius, 120)
      spider.penup()
  else:
    spider.setheading(angle*leg + 90)
    spider.pendown()
    spider.circle(radius, -120)
    spider.penup()

    leg = leg + 1

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()