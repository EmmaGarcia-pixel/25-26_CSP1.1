# import the turtle module
import turtle as trtl

# create the turtle object
painter = trtl.Turtle()

print("making a circle...")

# ask user for a color (such as red, green, blue, pink, purple)
color=input("What is your favorite color?")

# ask user for the radius of a circle
radius=input("What is your favorite number?")

# draw a circle with the radius and line color entered by the user
painter.color(color)
painter.circle(int(radius), 360, 5)

# get the screen object and make it persist
wn = trtl.Screen()
wn.mainloop()