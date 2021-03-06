from turtle import Turtle, mainloop
import random

class AnimatedTurtle(Turtle):
    
    allTurtles = []
    
    def __init__(self,hWall,vWall):
        super().__init__()
        self.scr = self.getscreen()
        self.xmin = -vWall+10
        self.xmax = vWall-10
        self.ymin = -hWall+10
        self.ymax = hWall-10
        self.scr.ontimer(self.__moveOneStep,100)  
        AnimatedTurtle.allTurtles.append(self)

    def __moveOneStep(self):
        self.__computeNewHeading()
        self.forward(5)
        self.__checkCollisions()
        self.scr.ontimer(self.__moveOneStep,100)

    def __computeNewHeading(self):
        xpos,ypos = self.position()
        oldHead = self.heading()
        newHead = oldHead

        if xpos > self.xmax or xpos < self.xmin:
            newHead = 180-oldHead
        if  ypos > self.ymax or ypos < self.ymin:
            newHead = 360-oldHead
        if newHead != oldHead:
            self.setheading(newHead)

    def __checkCollisions(self):
        for otherT in AnimatedTurtle.allTurtles:
            if self != otherT:
                if self.distance(otherT) < 20:
                    tempHeading = self.heading()
                    self.setheading(otherT.heading())
                    otherT.setheading(tempHeading)
                    while self.distance(otherT) < 20:
                        self.forward(1)
                        otherT.forward(1)

class TurtlePlace:
    def __init__(self,maxTurtles,hWall=200,vWall=200):
        self.bigT = Turtle()
        self.bigTscreen = self.bigT.getscreen()
        self.bigT.shape('turtle')
        self.turtleList = []
        self.bigTscreen.onclick(self.placeTurtle)
        self.bigT.hideturtle()
        self.numTurtles = 0
        self.maxTurtles = maxTurtles
        self.hWall = hWall
        self.vWall = vWall
        self.drawField(hWall,vWall)
        mainloop()

    def placeTurtle(self,x,y):
        newT = AnimatedTurtle(self.hWall,self.vWall)
        newTscreen = newT.getscreen()
        newTscreen.tracer(0)
        newT.up()
        newT.goto(x,y)
        newT.shape('turtle')
        newT.setheading(random.randint(1,359))
        newTscreen.tracer(1)
        self.numTurtles = self.numTurtles + 1
        self.turtleList.append(newT)
        if self.numTurtles >= self.maxTurtles:
            self.bigTscreen.onclick(None)

    def drawField(self,hWall,vWall):
        self.bigTscreen.tracer(0)
        self.bigT.up()
        self.bigT.goto(-hWall,-vWall)
        self.bigT.down()
        for i in range(4):
            self.bigT.forward(2*hWall)
            self.bigT.left(90)
        self.bigTscreen.tracer(1)

at = TurtlePlace(5,200,200)