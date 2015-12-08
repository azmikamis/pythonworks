import turtle

class Canvas:
    def __init__(self,w,h):
        self.width = w
        self.height = h
        self.visibleObjects = []
        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        self.screen.setup(width=self.width,height=self.height)
        self.turtle.hideturtle()

    def drawAll(self):
        self.screen.reset()
        self.screen.tracer(0)
        for shape in self.visibleObjects:
            shape._draw(self.turtle)
        self.screen.tracer(1)
        self.turtle.hideturtle()

    def addShape(self,shape):
        self.visibleObjects.append(shape)

    def draw(self,gObject):
        gObject.setCanvas(self)
        gObject.setVisible(True)
        self.turtle.up()
        self.screen.tracer(0)
        gObject._draw(self.turtle)
        self.screen.tracer(1)
        self.addShape(gObject)
        
    def freeze(self):
        self.screen.exitonclick()

class GeometricObject:

    def __init__(self):
        self.lineColor = 'black'
        self.lineWidth = 1
        self.visible = False
        self.myCanvas = None

    def setColor(self,color):
        self.lineColor = color
        if self.visible:
            self.myCanvas.drawAll()

    def setWidth(self,width):
        self.lineWidth = width
        if self.visible:
            self.myCanvas.drawAll()

    def getColor(self):
        return self.lineColor

    def getWidth(self):
        return self.lineWidth

    def _draw(self):
        print ("Error: You must define _draw in subclass")

    def setVisible(self,vFlag):
        self.visible = vFlag

    def setCanvas(self,theCanvas):
        self.myCanvas = theCanvas

        
class Point(GeometricObject):
    def __init__(self, x,y):
        super().__init__()
        self.x = x
        self.y = y

    def getCoord(self):
        return (self.x,self.y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def _draw(self,aturtle):
        aturtle.goto(self.x,self.y)
        aturtle.dot(self.lineWidth,self.lineColor)        

class Line(GeometricObject):
    def __init__(self, p1,p2):
        super().__init__()
        self.p1 = p1
        self.p2 = p2
    
    def getP1(self):
        return self.p1
        
    def getP2(self):
        return self.p2
        
    def _draw(self,aturtle):
        aturtle.color(self.getColor())
        aturtle.width(self.getWidth())
        aturtle.goto(self.p1.getCoord())
        aturtle.down()
        aturtle.goto(self.p2.getCoord())

class Shape(GeometricObject):
    def __init__(self):
        super().__init__()
        self.fillColor = None
        
    def setFill(self,acolor):
        self.fillColor=acolor
        if self.visible:
            self.myCanvas.drawAll()
    
class Polygon(Shape):
    def __init__(self,plist):
        super().__init__()
        self.corners = plist
        
    def _draw(self,aturtle):
        aturtle.color(self.getColor())
        aturtle.width(self.getWidth())
        aturtle.goto(self.corners[0].getCoord())
        aturtle.down()
        if self.fillColor:
            aturtle.fillcolor(self.fillColor)
            aturtle.begin_fill()
        for cindex in range(1,len(self.corners)):
            aturtle.goto(self.corners[cindex].getCoord())
        aturtle.goto(self.corners[0].getCoord())
        if self.fillColor:
            aturtle.end_fill()

def test():
	myCanvas = Canvas(800,600)
	
	myPoint = Point(100,100)
	myPoint.setColor("red")
	myPoint.setWidth(10)
	myCanvas.draw(myPoint)
	myLine = Line(Point(-100,-100),myPoint)
	myLine.setColor("magenta")
	myLine.setWidth(5)
	myCanvas.draw(myLine)
	myCanvas.freeze()

def test2():
    myCanvas = Canvas(500,500)

    
    p1=Point(0,0)
    p2=Point(-25,-29)
    p3=Point(-23,24)
    
    t = Polygon([p1,p2,p3])
    t.setFill("blue")  #original fill is blue
    
    myCanvas.draw(t)
    
    myLine = Line(Point(-100,-100),Point(100,100))
    myOtherLine = Line(Point(-100,100),Point(100,-100))
    myLine.setWidth(4)
    myOtherLine.setWidth(4)
    myCanvas.draw(myLine)
    myCanvas.draw(myOtherLine)
    myLine.setColor('red')
    
    
    t.setFill("green") #switch to green
    
    myCanvas.freeze()

def drawHouse():
    #To complete this example will require creation of Rectangle and Circle
    
	myCanvas = Canvas(800,600)
	house = Rectangle(Point(-100,-100),Point(100,100))
	house.setFill('blue')
	door = Rectangle(Point(-50,-100),Point(0,75))
	door.setFill('brown')
	roof1 = Line(Point(-100,100),Point(0,200))
	roof2 = Line(Point(0,200),Point(100,100))
	roof1.setWidth(3)
	roof2.setWidth(3)
	myCanvas.draw(house)
	myCanvas.draw(door)
	myCanvas.draw(roof1)
	myCanvas.draw(roof2)
	sun = Circle(Point(-150,250),20)
	sun.setFill('yellow')
	myCanvas.draw(sun)
	
#drawHouse()	
test2()