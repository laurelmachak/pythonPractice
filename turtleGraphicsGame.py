import turtle
import math
import random

#set up screen
wn = turtle.Screen()
wn.bgpic("pixelSpaceBackground.gif")
wn.tracer(3)

#Draw Border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

#Create player turtle
player = turtle.Turtle()
player.color("LightSteelBlue")
player.shape("triangle")
player.penup()
player.speed(0)

#create multiple goals

maxGoals = 6
goals = []

for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].color("OliveDrab")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-300,300), random.randint(-300,300))

#Set speed variable
pace = 1

#Define functions

def turnLeft():
    player.left(30)
    
def turnRight():
    player.right(30)
    
def increasePace():
    global pace
    pace += 1
    
def decreasePace():
    global pace
    if pace > 1:
        pace -= 1
        
def isCollision(t1,t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 20:
        return True
    else:
        return False


#set keyboard bindings
turtle.listen()
turtle.onkey(turnLeft, "Left")
turtle.onkey(turnRight, "Right")
turtle.onkey(increasePace, "Up")
turtle.onkey(decreasePace, "Down")


while True:
    player.forward(pace)
    #player boundary check
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)
        
    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)
        
    

    #move the goal
    for count in range(maxGoals):
        goals[count].forward(3)
    
        #goal boundary check
        if goals[count].xcor() > 290 or goals[count].xcor() < -290:
            goals[count].right(180)
        
        if goals[count].ycor() > 290 or goals[count].ycor() < -290:
            goals[count].right(180)
        #collision checking
        if isCollision(player,goals[count]):
            goals[count].setposition(random.randint(-290,290), random.randint(-290,290))
            goals[count].right(random.randint(0,360))
    
    
    

delay = input("press enter to finish")