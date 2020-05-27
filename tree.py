import turtle

#Initialize screen
playground = turtle.Screen() 

#Window name
playground.title("Fractal Tree")
playground.screensize(2000,1500)
playground.bgcolor("#4ecdc4")

#Initialize turtle
myTurtle = turtle.Turtle()

#Tree setup
myTurtle.setheading(90)
myTurtle.pencolor("#33001a")
myTurtle.pensize(1)
myTurtle.speed(9000)

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
        flowers()
        myTurtle.pendown()
        myTurtle.pencolor("#33001a")

#Flowers for the tree
def flowers():
    if (myTurtle.ycor() < 110):  
        myTurtle.penup()
    else:
         spring()

#Spring flowers
def spring():
    myTurtle.color("#3d2645", "#3d2645")
    myTurtle.begin_fill()
    myTurtle.circle(10)
    myTurtle.end_fill()
    myTurtle.left(45)    
    myTurtle.color("#da4167", "#da4167")
    myTurtle.begin_fill()
    myTurtle.circle(8)
    myTurtle.end_fill() 
    myTurtle.left(45)
    myTurtle.color("#f391a0", "#f391a0")
    myTurtle.begin_fill()
    myTurtle.circle(6)
    myTurtle.end_fill() 
    myTurtle.left(45) 
    myTurtle.color("#ff9f1c", "#ff9f1c")
    myTurtle.begin_fill()
    myTurtle.circle(2)
    myTurtle.end_fill() 
    myTurtle.right(135)  

#Call function
tree(100)

#Click to exit screen
playground.exitonclick() 