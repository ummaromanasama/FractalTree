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
myTurtle.speed(1000)

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
        # no_flower()
        flower()
        myTurtle.pencolor("#774936")

#Flowers for the tree
def flower():
    #Flower
    myTurtle.color("pink", "pink")
    myTurtle.begin_fill()
    myTurtle.circle(5)
    myTurtle.end_fill()
    #Another way to create the flowers
    # myTurtle.dot()

#Use to get the coordinates of the turtle
def myTurtle_location():
    location = myTurtle.pos()           
    myTurtle.write(str(location), True) 
    print(location)     

#Get ride of flowers in unnecessary locations
#Think I'm going to need to combine the flower() and
#no_flower because they go hand in hand
def no_flower():
    if (myTurtle.ycor() < 100):  
        myTurtle.penup()
    
    
#Call function
tree(100)

#Click to exit screen
playground.exitonclick() 