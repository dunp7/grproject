from turtle import Screen, Turtle
from colorsys import hsv_to_rgb

RADIUS = 100
NUMBER_OF_WEDGES = 20
SLICE_ANGLE = 360 / NUMBER_OF_WEDGES

screen = Screen()
screen.tracer(False)

turtle = Turtle(visible=False)
turtle.penup()
center = turtle.position()

turtle.sety(turtle.ycor() - RADIUS)

hues = [color / NUMBER_OF_WEDGES for color in range(NUMBER_OF_WEDGES)]  # precompute hues

index = 0

def draw_circle():
    global index

    for hue in range(NUMBER_OF_WEDGES):
        turtle.color(hsv_to_rgb(hues[(hue + index) % NUMBER_OF_WEDGES], 1.0, 1.0))

        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(RADIUS, extent=SLICE_ANGLE)
        position = turtle.position()
        turtle.goto(center)
        turtle.end_fill()
        turtle.penup()

        turtle.goto(position)

    screen.update()
    index = (index + 1) % NUMBER_OF_WEDGES
    screen.ontimer(draw_circle, 40)

draw_circle()

screen.exitonclick()