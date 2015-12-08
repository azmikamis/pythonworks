from turtle import Turtle, mainloop

class Etch(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = self.getscreen()
        self.color('blue')
        self.pensize(2)
        self.speed(0)
        self.distance = 5
        self.turn = 10
        self.screen.onkey(self.fwd,"Up")
        self.screen.onkey(self.bkwd,"Down")
        self.screen.onkey(self.left5,"Left")
        self.screen.onkey(self.right5,"Right")
        self.screen.onkey(self.quit,"q")
        self.screen.listen()        
        self.main()

    def fwd(self):
        self.forward(self.distance)

    def bkwd(self):
        self.backward(self.distance)

    def left5(self):
        self.left(self.turn)

    def right5(self):
        self.right(self.turn)

    def quit(self):
        self.screen.bye()

    def main(self):
        mainloop()

if __name__ == '__main__':
    etch = Etch()