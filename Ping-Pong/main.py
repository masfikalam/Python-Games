import turtle

# game window
win = turtle.Screen()
win.setup(width=800, height=600)
win.bgcolor('#b0ca85')
win.title("Ping Pong 2D")
win.tracer(0)

# player scores
score_a = 0
score_b = 0
score = turtle.Turtle()
score.speed(0)
score.color('#212220')
score.hideturtle()
score.penup()
score.goto(0, 260)
score.write(f"{score_a} : {score_b}", align='center', font=('Courier', 24, 'bold'))

# player A
player_a = turtle.Turtle()
player_a.speed(0)
player_a.shape('square')
player_a.color('#212220')
player_a.shapesize(stretch_wid=4, stretch_len=1)
player_a.penup()
player_a.goto(-350, 0)

# player B
player_b = turtle.Turtle()
player_b.speed(0)
player_b.shape('square')
player_b.color('#212220')
player_b.shapesize(stretch_wid=4, stretch_len=1)
player_b.penup()
player_b.goto(350, 0)

# game ball
ball = turtle.Turtle()
ball.dx = 0.07
ball.dy = 0.07
ball.speed(0)
ball.shape('circle')
ball.color('#212220')
ball.penup()
ball.goto(0, 0)

# functions
def a_up():
    y = player_a.ycor()
    if y >= 245: y = 245
    else : player_a.sety(y + 30)

def a_down():
    y = player_a.ycor()
    if y <= -230: y = -230
    player_a.sety(y - 30)

def b_up():
    y = player_b.ycor()
    if y >= 245: y = 245
    player_b.sety(y + 30)

def b_down():
    y = player_b.ycor()
    if y <= -230: y = -230
    player_b.sety(y - 30)

# key events
win.listen()
win.onkeypress(a_up, 'w')
win.onkeypress(b_up, 'Up')
win.onkeypress(a_down, 's')
win.onkeypress(b_down, 'Down')

# game loop
while True:
    win.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # touch borders
    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() <= -290:
        ball.sety(-290)
        ball.dy *= -1

    # touch fences
    if ball.xcor() >= 390:
        score_a += 1
        ball.goto(0,0)
        ball.dx *= -1
        score.clear()
        score.write(f"{score_a} : {score_b}", align='center', font=('Courier', 24, 'bold'))

    if ball.xcor() <= -390:
        score_b += 1
        ball.goto(0,0)
        ball.dx *= -1
        score.clear();
        score.write(f"{score_a} : {score_b}", align='center', font=('Courier', 24, 'bold'))
    
    # player_a bounce
    if (ball.xcor() <= -340 and ball.xcor() >= -350) and (ball.ycor() < player_a.ycor() + 40 and ball.ycor() > player_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    # player_b bounce
    if (ball.xcor() >= 340 and ball.xcor() <= 350) and (ball.ycor() < player_b.ycor() + 40 and ball.ycor() > player_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

