import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

    draw_square(100, "turtle", "yellow", 2)
    draw_circle(100, "circle", "blue", 2)
    draw_triangle(300, "triangle", "black", 2)

    window.exitonclick()
    
def draw_square(size, shape, color, speed):
    newSquare = turtle.Turtle()
    newSquare.shape(shape)
    newSquare.color(color)
    newSquare.speed(speed)
    i = 0
    while (i<4):
        newSquare.forward(size)
        newSquare.right(90)
        i+=1

def draw_circle(radius, shape, color, speed):
    newCircle = turtle.Turtle()
    newCircle.shape(shape)
    newCircle.color(color)
    newCircle.speed(speed)
    newCircle.circle(radius)

def draw_triangle(size, shape, color, speed):
    newTriangle = turtle.Turtle()
    newTriangle.shape(shape)
    newTriangle.color(color)
    newTriangle.speed(speed)
    j=0
    while (j<3):
        newTriangle.backward(size)
        newTriangle.right(120)
        j+=1
    
draw_shapes()
