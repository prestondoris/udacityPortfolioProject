import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    rosie = turtle.Turtle()
    luna = turtle.Turtle()

    for i in range(1, 37):
        draw_square(brad, 100, "turtle", "yellow", 10)
        brad.right(10)
        
    #draw_circle(rosie, 100, "circle", "blue", 2)
    #draw_triangle(luna, 300, "triangle", "black", 2)

    window.exitonclick()
    
def draw_square(newSquare, size, shape, color, speed):
    newSquare.shape(shape)
    newSquare.color(color)
    newSquare.speed(speed)
    i = 0
    while (i<4):
        newSquare.forward(size)
        newSquare.right(90)
        i+=1

def draw_circle(newCircle, radius, shape, color, speed):
    newCircle.shape(shape)
    newCircle.color(color)
    newCircle.speed(speed)
    newCircle.circle(radius)

def draw_triangle(newTriangle, size, shape, color, speed):
    newTriangle.shape(shape)
    newTriangle.color(color)
    newTriangle.speed(speed)
    j=0
    while (j<3):
        newTriangle.backward(size)
        newTriangle.right(120)
        j+=1
    
draw_shapes()
