

import turtle 

#Sets up the screen and the "turtle" the way I want it


scr = turtle.Screen()
turtle.begin_fill()
scr.bgcolor("black")


turtle.color("red")
turtle.shape("triangle")
turtle.turtlesize(0.5,1)
turtle.fillcolor("red")

#Lengths

length1 = -100
length2 = 5
angle = 60

#Loop

for x in range(25):
    turtle.forward(length1)
    turtle.left(angle)
    turtle.right(length2)

turtle.end_fill()

#Moving Turtle to a different location==========================================

turtle.home()

turtle.penup()
turtle.forward(250)
turtle.pendown()

# Set the turtle how I want it. ================================================================
turtle.begin_fill()
turtle.color("orange")
turtle.shape("circle")
turtle.left(180)
turtle.turtlesize(0.5,1)

#More Lengths

length1 = -25
length2 = 15
length3 = 10
angle = 35

#Another Loop

for x in range(20):
    turtle.forward(length1)
    turtle.left(angle)
    turtle.forward(length3)
    turtle.right(length2)

turtle.end_fill()

# Moving Turtle Again======================================

turtle.left(90)
turtle.penup()
turtle.forward(-300)
turtle.pendown()

turtle.penup()
turtle.forward(-50)
turtle.pendown()
#=================================================
# Setting turtle again bla bla bla im pretty sure you can figure it out now.

turtle.begin_fill()
turtle.color("dark orange")
turtle.shape("circle")
turtle.left(-180)
turtle.turtlesize(0.5,1)



length1 = -25
length2 = 15
length3 = 10
angle = 35

#Another Loop
for x in range(20):
    turtle.forward(length1)
    turtle.left(angle)
    turtle.forward(length3)
    turtle.right(length2)

turtle.end_fill()

#============================================================

turtle.penup()
turtle.forward(250)
turtle.pendown()

#=====================================================================

turtle.begin_fill()
turtle.color("blue")
turtle.shape("arrow")
turtle.left(-180)
turtle.turtlesize(0.5,1)



length1 = -75
length2 = 55
length3 = 10
angle = 35

#Another Loop
for x in range(17):
    turtle.forward(length1)
    turtle.left(angle)
    turtle.forward(length3)
    turtle.right(length2)

turtle.end_fill()
#=====================================================================





turtle.done()
