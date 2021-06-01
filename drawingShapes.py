import turtle

t = turtle.Turtle()
t.speed(10)
size = 300
t.hideturtle()


def clear():
    t.clear()
    t.hideturtle()


def square():
    for i in range(4):
        t.forward(size)
        t.left(90)


def rectangle():
    side_a = size
    side_b = size / 2
    t.forward(side_a)
    t.left(90)
    t.forward(side_b)
    t.left(90)
    t.forward(side_a)
    t.left(90)
    t.forward(side_b)
    t.left(90)


def hexagon():
    t.up()
    t.goto(-size / 4, -size / 4)
    t.down()
    for i in range(6):
        t.forward(size / 2)
        t.left(60)


def triangle():
    for _ in range(3):
        t.forward(size)
        t.right(-120)


def star():
    t.left(36)
    t.up()
    t.goto(-144, -144)
    t.down()
    for _ in range(5):
        t.forward(144)
        t.up()
        t.forward(92)
        t.down()
        t.forward(144)
        t.left(144)


def turtleLabel(colors, shapes, message):
    t.clear()
    t.up()
    t.goto(-400, 350)
    t.write(message)


def draw(shape, color="white"):
    t.up()
    t.goto(-(size / 2), -(size / 2))

    try:
        t.fillcolor(color)
        print("Color: " + color)
    except Exception as e:
        t.write("Sorry, could not recognize what you've said, try once again.")

    t.down()
    t.begin_fill()

    if(shape == "circle"):
        t.up()
        t.goto(0, 0)
        t.down()
        t.circle(size / 2)

    elif(shape == "square"):
        square()

    elif(shape == "triangle"):
        triangle()

    elif(shape == "star"):
        star()

    elif(shape == "rectangle"):
        rectangle()

    elif(shape == "hexagon"):
        hexagon()

    else:
        t.write("Sorry, could not recognize what you've said, try once again.")

    t.end_fill()
