import turtle

class Etch:
    def __init__(self):
        self.myT = turtle.Turtle()
        self.myScreen = turtle.Screen()
        self.myT.color('blue')
        self.myT.pensize(2)
        self.myT.speed(0)
        self.distance = 5
        self.turn = 10
        self.myScreen.onkey(self.fwd,"Up")
        self.myScreen.onkey(self.bkwd,"Down")
        self.myScreen.onkey(self.left,"Left")
        self.myScreen.onkey(self.right,"Right")
        self.myScreen.onkey(self.quit,"q")
        self.myScreen.listen()

    def fwd(self):
        self.myT.forward(self.distance)

    def bkwd(self):
        self.myT.backward(self.distance)

    def left(self):
        self.myT.left(self.turn)

    def right(self):
        self.myT.right(self.turn)

    def quit(self):
        self.myScreen.bye()

    def main(self):
        turtle.mainloop()
