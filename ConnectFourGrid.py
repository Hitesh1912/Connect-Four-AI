import turtle, time


def printing_on_screen(x, y, z):
    turtle.tracer(0, 0)
    screen_limit(7, 6)
    empty_grid()
    if z == 1:
        agent_circle(y, x)
    if z == 2:
        player_circle(y, x)
    turtle.update()
    # time.sleep(2)


def screen_limit(w, h):
    turtle.setup(width=w * 75, height=h * 75)
    turtle.setworldcoordinates(-0.2, -0.2, w, h)


def empty_grid():
    for i in range(7):
        turtle.pu()
        turtle.goto(i, 0)
        turtle.setheading(90)
        turtle.pd()
        turtle.forward(8)

    for i in range(7):
        turtle.pu()
        turtle.goto(i - 4, -0.2)
        turtle.setheading(0)
        turtle.forward(4.5)
        turtle.pd()
        turtle.write(i)

    for i in range(6):
        turtle.pu()
        turtle.goto(0, i)
        turtle.setheading(0)
        turtle.pd()
        turtle.forward(8)

    turtle.pu()


def agent_circle(x, y):
    turtle.pencolor("blue")
    turtle.fillcolor("blue")
    turtle.goto(x + 0.5, y + 0.2)
    turtle.begin_fill()
    turtle.pd()
    turtle.circle(0.3)
    turtle.end_fill()
    turtle.pu()


def player_circle(x, y):
    turtle.pencolor("red")
    turtle.fillcolor("red")
    turtle.goto(x + 0.5, y + 0.2)
    turtle.begin_fill()
    turtle.pd()
    turtle.circle(0.3)
    turtle.end_fill()
    turtle.pu()
