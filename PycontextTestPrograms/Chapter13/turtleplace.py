from turtle import Turtle, mainloop
import random

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
        newT = Turtle()
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

tp = TurtlePlace(5)