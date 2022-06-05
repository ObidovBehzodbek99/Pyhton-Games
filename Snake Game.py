import time
import turtle
import random

delay = 0.1

window = turtle.Screen()
window.title('Snake Game')
window.setup(width=500, height=500)
window.bgcolor('orange')
window.tracer(0)

score = turtle.Turtle()
score.speed(0)
score.penup()
score.goto(0, 200)
score.hideturtle()
score.write('Score: 0            High Score: 0', align='center', font=('Arial', 24, 'normal'))

current_score = 0
high_score = 0

wall = turtle.Turtle()
wall.speed(0)
wall.penup()
wall.goto(0, 185)
wall.color('white')
wall.shape('square')
wall.shapesize(stretch_wid=0.1, stretch_len=25)

x = random.randint(-240, 240)
y = random.randint(-240, 180)

food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(x, y)
food.shapesize(stretch_wid=0.5, stretch_len=0.5)

head = turtle.Turtle()
head.speed(0)
head.shape('triangle')
head.color('green')
head.penup()
head.goto(0, 0)
head.shapesize(stretch_wid=0.8, stretch_len=0.8)
head.direction = 'stop'

def begin(x, y):
    start.shapesize(stretch_wid=0.0001, stretch_len=0.0001)

start = turtle.Turtle()
start.hideturtle()
start.speed(0)
start.shape('triangle')
start.color('green')
start.shapesize(stretch_wid=4, stretch_len=4)
start.penup()
start.goto(0, 0)
start.onclick(begin)
start.showturtle()

def turn_up():
    if head.direction != "down":
        head.direction = "up"
        head.settiltangle(90)
def turn_down():
    if head.direction != "up":
        head.direction = "down"
        head.settiltangle(270)
def turn_left():
    if head.direction != "right":
        head.direction = "left"
        head.settiltangle(180)
def turn_right():
    if head.direction != "left":
        head.direction = "right"
        head.settiltangle(0)

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

window.listen()
window.onkeypress(turn_right, 'Right')
window.onkeypress(turn_left, 'Left')
window.onkeypress(turn_up, 'Up')
window.onkeypress(turn_down, 'Down')

segments = []

while True:
    window.update()


    if head.xcor() > 240:
        y = head.ycor()
        head.goto(-240, y)
    if head.xcor() < -240:
        y = head.ycor()
        head.goto(240, y)
    if head.ycor() > 180:
        x = head.xcor()
        head.goto(x, -240)
    if head.ycor() < -240:
        x = head.xcor()
        head.goto(x, 180)

    if head.distance(food) < 20:
        x = random.randint(-240, 240)
        y = random.randint(-240, 180)
        food.goto(x, y)

        segment = turtle.Turtle()
        segment.speed(0)
        segment.color('green')
        segment.shape('circle')
        segment.shapesize(stretch_wid=0.5, stretch_len=0.5)
        segment.penup()
        segments.append(segment)

        delay -= 0.0001
        current_score += 1

        if current_score > high_score:
            high_score = current_score
        score.clear()
        score.write('Score: {}            High Score: {}'.format(current_score, high_score), align='center',
                    font=('Arial', 24, 'normal'))

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            head.direction = 'stop'
            head.goto(0, 0)

            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()

            current_score = 0
            score.clear()
            score.write('Score: {}            High Score: {}'.format(current_score, high_score), align='center',
                        font=('Arial', 24, 'normal'))

            end = turtle.Turtle()
            end.speed(0)
            end.penup()
            end.hideturtle()
            end.goto(0, 50)
            end.write('Game Over!', align='center', font=('Arail', 50, 'normal'))

    time.sleep(delay)

window.mainloop()