import turtle


def tegn_firkant(sidelengde):
    turtle.forward(sidelengde)
    turtle.left(90)
    turtle.forward(sidelengde)
    turtle.left(90)
    turtle.forward(sidelengde)
    turtle.left(90)
    turtle.forward(sidelengde)
    turtle.left(90)


turtle.setup(600, 600, 120, 20)
tegn_firkant(100)

turtle.done()
