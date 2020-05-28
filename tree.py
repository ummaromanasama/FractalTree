import turtle

#Initialize screen
playground = turtle.Screen() 

#Window name
playground.title("Fractal Tree")
playground.screensize(2000,1500)
playground.bgcolor("#f3e9d2")

#Initialize turtle
myTurtle = turtle.Turtle()

#Tree setup
myTurtle.setheading(90)
myTurtle.pencolor("#114b5f")
myTurtle.pensize(1)
myTurtle.speed(100)

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
        myTurtle.pencolor("#114b5f")

#Flowers for the tree
def flowers():
    if (myTurtle.ycor() < 110):  
        myTurtle.penup()
    else:
        # spring()
        # summer()
        # fall()
        # winter()
        default()

#Flowers patterns
def spring():
    myTurtle.color("#450920", "#450920")
    myTurtle.begin_fill()
    myTurtle.circle(10)
    myTurtle.end_fill()
    myTurtle.left(0)    
    myTurtle.color("#a53860", "#a53860")
    myTurtle.begin_fill()
    myTurtle.circle(8)
    myTurtle.end_fill() 
    myTurtle.left(90)
    myTurtle.color("#da627d", "#da627d")
    myTurtle.begin_fill()
    myTurtle.circle(6)
    myTurtle.end_fill() 
    myTurtle.left(180) 
    myTurtle.color("#ffa5ab", "#ffa5ab")
    myTurtle.begin_fill()
    myTurtle.circle(4)
    myTurtle.end_fill() 
    myTurtle.left(270) 
    myTurtle.color("#fcbf49", "#fcbf49")
    myTurtle.begin_fill()
    myTurtle.circle(2)
    myTurtle.end_fill() 
    myTurtle.right(540)  

def summer():
    myTurtle.color("#9d0208", "#9d0208")
    myTurtle.begin_fill()
    myTurtle.circle(10)
    myTurtle.end_fill()
    myTurtle.left(0)    
    myTurtle.color("#ffc107", "#ffc107")
    myTurtle.begin_fill()
    myTurtle.circle(8)
    myTurtle.end_fill() 
    myTurtle.left(90)
    myTurtle.color("#ffd11e", "#ffd11e")
    myTurtle.begin_fill()
    myTurtle.circle(6)
    myTurtle.end_fill() 
    myTurtle.left(180) 
    myTurtle.color("#ffe035", "#ffe035")
    myTurtle.begin_fill()
    myTurtle.circle(4)
    myTurtle.end_fill() 
    myTurtle.left(270) 
    myTurtle.color("#827752", "#827752")
    myTurtle.begin_fill()
    myTurtle.circle(2)
    myTurtle.end_fill() 
    myTurtle.right(540)

def fall():
    myTurtle.color("#220901", "#220901")
    myTurtle.begin_fill()
    myTurtle.circle(10)
    myTurtle.end_fill()
    myTurtle.left(0)    
    myTurtle.color("#621708", "#621708")
    myTurtle.begin_fill()
    myTurtle.circle(8)
    myTurtle.end_fill() 
    myTurtle.left(90)
    myTurtle.color("#941b0c", "#941b0c")
    myTurtle.begin_fill()
    myTurtle.circle(6)
    myTurtle.end_fill() 
    myTurtle.left(180) 
    myTurtle.color("#bc3908", "#bc3908")
    myTurtle.begin_fill()
    myTurtle.circle(4)
    myTurtle.end_fill() 
    myTurtle.left(270) 
    myTurtle.color("#f6aa1c", "#f6aa1c")
    myTurtle.begin_fill()
    myTurtle.circle(2)
    myTurtle.end_fill() 
    myTurtle.right(540)

def winter():
    myTurtle.color("#003049", "#003049")
    myTurtle.begin_fill()
    myTurtle.circle(10)
    myTurtle.end_fill()
    myTurtle.left(0)    
    myTurtle.color("#3d5a80", "#3d5a80")
    myTurtle.begin_fill()
    myTurtle.circle(8)
    myTurtle.end_fill() 
    myTurtle.left(90)
    myTurtle.color("#98c1d9", "#98c1d9")
    myTurtle.begin_fill()
    myTurtle.circle(6)
    myTurtle.end_fill() 
    myTurtle.left(180) 
    myTurtle.color("#90e0ef", "#90e0ef")
    myTurtle.begin_fill()
    myTurtle.circle(4)
    myTurtle.end_fill() 
    myTurtle.left(270) 
    myTurtle.color("#e0fbfc", "#e0fbfc")
    myTurtle.begin_fill()
    myTurtle.circle(2)
    myTurtle.end_fill() 
    myTurtle.right(540)

def default():
    myTurtle.color("#0c5e50", "#88d498")
    myTurtle.begin_fill()
    myTurtle.circle(10)
    myTurtle.end_fill()

#Call function
tree(100)

#Click to exit screen
playground.exitonclick() 