import turtle

def draw():
    window = turtle.Screen()
    charles = turtle.Turtle()

    for i in range(1,150):
        #draw triangle
        triangle(charles)
        #rotate charles
        charles.right(5)
    charles.home()
    charles.right(90)
    charles.forward(400)
        
    window.exitonclick()

def triangle(newTriangle):
    newTriangle.speed(200)
    newTriangle.forward(100)
    newTriangle.left(99.594)
    newTriangle.forward(300)
    newTriangle.left(160.812)
    newTriangle.forward(300)

draw()
