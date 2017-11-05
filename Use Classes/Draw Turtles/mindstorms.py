import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    i = 0
    while (i<4):
        brad.forward(100)
        brad.right(90)
        i+=1

    rosie = turtle.Turtle()
    rosie.shape("arrow")
    rosie.color("blue")
    rosie.circle(100)

    luna = turtle.Turtle()
    j=0
    while (j<3):
        luna.forward(100)
        luna.right(120)
        j+=1
    

    window.exitonclick()

draw_shapes()
