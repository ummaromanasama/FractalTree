import turtle

#Initialize screen
playground = turtle.Screen() 

#Window name
playground.title("Fractal Tree")
playground.screensize(2000,1500)
# playground.bgcolor("#197278")

#Initialize turtle
myTurtle = turtle.Turtle()

#Tree setup
myTurtle.setheading(90)
myTurtle.pencolor("#774936")
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
        flower()
        myTurtle.pendown()
        myTurtle.pencolor("#774936")

#Flowers for the tree
def flower():
    #I need to account for the rest of the values
    #Negative/postive and x/y values
    if (myTurtle.xcor() > 100):  
        myTurtle.penup()
    else:
        myTurtle.color("pink", "pink")
        myTurtle.begin_fill()
        myTurtle.circle(5)
        myTurtle.end_fill()

#Use to get the coordinates of the turtle
def myTurtle_location():
    location = myTurtle.pos()           
    myTurtle.write(str(location), True) 
    print(location)       
    
#Call function
tree(100)

#Click to exit screen
playground.exitonclick() 