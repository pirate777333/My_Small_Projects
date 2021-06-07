import turtle
import random

wn = turtle.Screen()
wn.title("snake game")
wn.bgcolor("green")
wn.setup(width=600, height=600)

head = turtle.Turtle()
head.ht()
head.speed(1)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"
head.write("press space to start", font=("Verdana",
                                    20, "normal"),align='center')

#head.goto(300, 300)
#head.goto(0, 0)


def up():
    head.setheading(90)
    #head.forward(100)

def down():
    head.setheading(270)
    #head.forward(100)

def left():
    head.setheading(180)
    #head.forward(100)

def right():
    head.setheading(0)
    #head.forward(100)

turtle.listen()

turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")

def start():
    head.clear()
    head.showturtle()

    leaf=turtle.Turtle()
    leaf.color("red")
    leaf.shape("turtle")
    leaf.penup()
    leaf.goto(random.randint(-290,290), random.randint(-290,290))
    b=1
    while True:
        head.forward(10)

        if head.position()[0]>=300 or head.position()[0]<=-300 or head.position()[1]>=300 or head.position()[1]<=-300:
            break
        if leaf.position()[0]-20<=head.position()[0]<=leaf.position()[0]+20 and leaf.position()[1]-20<=head.position()[1]<=leaf.position()[1]+20:
            
            leaf.goto(random.randint(-290,290), random.randint(-290,290))
            head.shapesize(stretch_len=b)
            b+=1

    wn = turtle.Screen()
    wn.title("snake game")
    wn.bgcolor("green")
    wn.setup(width=600, height=600)
    head.ht()
    head.speed(0)
    head.goto(0, 0)
    head.write("game over", font=("Verdana",
                                        20, "normal"),align='center')

turtle.onkey(start, "space")

turtle.mainloop()
