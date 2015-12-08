import turtle

def applyProduction(axiom,rules,n):
    for i in range(n):
        newString = ""
        for ch in axiom:
            newString = newString + rules.get(ch,ch)  
        axiom = newString
    return axiom

def drawLS(aTurtle,instructions,angle,distance):
    stateSaver = []
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == '[':
            pos = aTurtle.position()
            head = aTurtle.heading()
            stateSaver.append((pos,head))
        elif cmd == ']':
            pos,head = stateSaver.pop()
            aTurtle.up()
            aTurtle.setposition(pos)
            aTurtle.setheading(head)
            aTurtle.down()
            
            
def lsystem(axiom,rules,depth,initialPosition,heading,angle,length):
    aTurtle = turtle.Turtle()
    win = turtle.Screen()
    win.tracer(0)
    aTurtle.up()
    aTurtle.setposition(initialPosition)
    aTurtle.down()
    aTurtle.setheading(heading)
    newRules = applyProduction(axiom,rules,depth)
    print(newRules)
    drawLS(aTurtle,newRules,angle,length)
    win.tracer(1)
    win.exitonclick() 

axiom = 'H'
myRules = {'H':'HFH[+H][-H]',
           'X':'X[-FFF][+FFF]FX'}

lsystem(axiom,myRules,7,(0,-200),90,27.5,3)
