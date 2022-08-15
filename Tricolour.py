from time import time
import turtle
from turtle import*

# For output screen
screen = turtle.Screen()
screen.bgcolor("#dbe4ff")
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)

# Defining a turtle Instance
t = turtle.Turtle()
t.shape("turtle")
t.speed(3)

# Starting position of turtle
t.penup()

# Orange rectangle
t.goto(-315,200)
t.color("orange")
t.pendown()
t.begin_fill()
t.forward(630)
t.right(90)
t.forward(130)
t.right(90)
t.forward(630)
t.right(90)
t.forward(130)
t.end_fill()
t.backward(130)

# White rectangle
t.right(90)
t.color("white")
t.begin_fill()
t.forward(630)
t.right(90)
t.forward(140)
t.right(90)
t.forward(630)
t.right(90)
t.forward(140)
t.end_fill()
t.backward(140)

# Green rectangle
t.right(90)
t.color("green")
t.begin_fill()
t.forward(630)
t.right(90)
t.forward(130)
t.right(90)
t.forward(630)
t.right(90)
t.forward(130)
t.end_fill()

# Big Blue Circle
t.penup()
t.right(90)
t.goto(0, -70)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(70)
t.end_fill()

# Big White Circle
t.penup()
t.goto(0, -60)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(60)
t.end_fill()

# Mini Blue Circles
t.penup()
t.speed(0)
t.left(180)
t.goto(8, -57)
t.pendown()
t.color("navy")
for i in range(24):
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.penup()
    t.forward(15)
    t.right(15)
    t.pendown()

# Spokes
t.penup()
t.speed(3)
t.goto(0, 0)
t.pendown()
t.pensize(2)
t.left(105)
for i in range(24):
    t.forward(60)
    t.backward(60)
    t.right(15)

# Small Blue Circle
t.penup()
t.left(75)
t.goto(0, -10)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

# Text
t.hideturtle()
t.penup()
t.goto(-300, 200)
t.color("orange")
t.pendown()
t.write("Happy ", 
font=("Calibri", 35, "bold")
)
t.penup()
t.goto(-125, 200)
t.color("navy")
t.pendown()
t.write("Independence ", 
font=("Calibri", 35, "bold")
)
t.penup()
t.goto(200, 200)
t.color("green")
t.pendown()
t.write("Day!", 
font=("Calibri", 35, "bold")
)

t.hideturtle()
turtle.done()
