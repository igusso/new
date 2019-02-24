import turtle
import random
import time
x = 0

import os
wn = turtle.Screen ()
wn.title("JUMP!")
wn.setup(500,500)
wn.bgcolor("black")
wn.tracer(0)
score=0




#Speed values list
speedlist = [0.4, 0.5, 0.6, 0.3, 0.55]
colourList= ["white", "blue", "red", "green", "yellow", "purple"]

pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 100)
pen.write("SCORE: 0", align="center", font=("Courier", 24, "normal"))

#border
border = turtle.Turtle()
border.color("white")
border.shape("square")
border.penup()
border.goto(-200, 0)
border.pendown()
border.goto(200, 0)
border.hideturtle()

#Player
player = turtle.Turtle ()
player.color("red")
player.shape("triangle")
player.speed(0)
player.penup()
player.setheading(90)
player.goto(-100, 6)
player.dy = 0.08


#Object
object = turtle.Turtle()
object.speed(0)
object.color("White")
object.shape("square")
object.penup()
object.goto(200, 10)
object.dx = 0.4

def jump():
    if player.ycor() <9 and (player.ycor() >0):
        y = player.ycor()
        y += 50
        player.sety(y)
def cheat():
    x=0
    x+=5
    print(x)

#Key binding
wn.listen()
wn.onkeypress(jump, "space")
wn.onkeypress(cheat, "Up")

#Main Loop
while True:
    wn.update()
    object.setx(object.xcor() - object.dx)
    if player.ycor() > 6:
        player.sety(player.ycor() - player.dy)

    if player.ycor() > 55:
        player.sety(55)

    #objects return
    if object.xcor() < -210:
        object.dx = speedlist[random.randint(0,4)]
        object.setx(random.randint(190, 400))
        los = random.randint(0,5)
        object.color(colourList[los])
        pen.clear()
        score += 1
        pen.write("SCORE: {}".format(score), align="center", font=("Courier", 24, "normal"))

    #object off the screen
    if object.xcor() > 200:
        object.hideturtle()
    if object.xcor() < 200:
        object.showturtle()

     #collision
    if (object.xcor() < -90 and object.xcor() > -110) and (player.ycor() <22):
        object.setx(random.randint(200, 300))
        object.dx = 0.3
        pen.clear()
        score=0
        pen.write("TRY AGAIN!", align="center", font=("Courier", 24, "normal"))
        time.sleep(1)
    #cheat
   # if object.xcor() > 10 and (object.xcor()) < 20:
        y = player.ycor()
        y += 50
        player.sety(y)




