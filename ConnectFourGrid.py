import turtle,time

def screen_limit(w,h):
    turtle.setup(width=w*75,height=h*75)
    turtle.setworldcoordinates(0,0,w,h)

def empty_grid():
    for i in range(7):
        turtle.pu()
        turtle.goto(i,0)
        turtle.setheading(90)
        turtle.pd()
        turtle.forward(8)
    for i in range(6):
        turtle.pu()
        turtle.goto(0,i)
        turtle.setheading(0)
        turtle.pd()
        turtle.forward(8)
    turtle.pu()


def agent_circle(x, y):
    turtle.pencolor("blue")
    turtle.fillcolor("blue")
    turtle.goto(x+0.5, y+0.2)
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



def main():
    turtle.tracer(0, 0)
    screen_limit(7,6)
    empty_grid()
    agent_circle(0,0)
    player_circle(5,2)
    turtle.update()
    time.sleep(10)


if __name__ == '__main__':
    main()
