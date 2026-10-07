import turtle
import time

# ---------------- SCREEN ----------------
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# ---------------- LEFT PADDLE ----------------
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# ---------------- RIGHT PADDLE ----------------
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# ---------------- BALL ----------------
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.dx = 2
ball.dy = 2

# ---------------- SCORE ----------------
score_a = 0
score_b = 0

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 250)

score.write(
    "Player A: 0    Player B: 0",
    align="center",
    font=("Arial", 20, "normal")
)

# ---------------- FUNCTIONS ----------------

def left_up():
    y = left_paddle.ycor()

    if y < 250:
        left_paddle.sety(y + 20)


def left_down():
    y = left_paddle.ycor()

    if y > -250:
        left_paddle.sety(y - 20)


def right_up():
    y = right_paddle.ycor()

    if y < 250:
        right_paddle.sety(y + 20)


def right_down():
    y = right_paddle.ycor()

    if y > -250:
        right_paddle.sety(y - 20)


# ---------------- KEYBOARD ----------------

screen.listen()

screen.onkeypress(left_up, "w")
screen.onkeypress(left_down, "s")

screen.onkeypress(right_up, "Up")
screen.onkeypress(right_down, "Down")

# ---------------- GAME LOOP ----------------

while True:

    screen.update()

    time.sleep(0.01)

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top wall
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = -ball.dy

    # Bottom wall
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = -ball.dy

    # Right wall
    if ball.xcor() > 390:

        score_a += 1

        ball.goto(0, 0)
        ball.dx = -2
        ball.dy = 2

        score.clear()
        score.write(
            "Player A: " + str(score_a) +
            "    Player B: " + str(score_b),
            align="center",
            font=("Arial", 20, "normal")
        )

    # Left wall
    if ball.xcor() < -390:

        score_b += 1

        ball.goto(0, 0)
        ball.dx = 2
        ball.dy = 2

        score.clear()
        score.write(
            "Player A: " + str(score_a) +
            "    Player B: " + str(score_b),
            align="center",
            font=("Arial", 20, "normal")
        )

    # Right paddle collision
    if (
        ball.xcor() > 330
        and ball.xcor() < 350
        and ball.ycor() < right_paddle.ycor() + 50
        and ball.ycor() > right_paddle.ycor() - 50
    ):
        ball.setx(330)
        ball.dx = -ball.dx

    # Left paddle collision
    if (
        ball.xcor() < -330
        and ball.xcor() > -350
        and ball.ycor() < left_paddle.ycor() + 50
        and ball.ycor() > left_paddle.ycor() - 50
    ):
        ball.setx(-330)
        ball.dx = -ball.dx