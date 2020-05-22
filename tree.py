import turtle

#Initialize screen
screen = turtle.Screen() 

#Window name
turtle.title('Fractal Tree')

#Initialize turtle
myTurtle = turtle.Turtle()

#Tree setup
myTurtle.setheading(90)
myTurtle.pensize(1)
myTurtle.speed(700)

#Recursion tree
def tree(x):
    if(x<10):
        return
    else:
        myTurtle.forward(x)
        myTurtle.left(30)
        tree(3*x/4)
        myTurtle.right(60)
        tree(3*x/4)
        myTurtle.left(30)
        myTurtle.backward(x)

#Call function
tree(100)

#Click to exit screen
screen.exitonclick() 