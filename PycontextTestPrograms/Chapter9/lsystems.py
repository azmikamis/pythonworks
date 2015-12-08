import turtle

def applyProduction(axiom,rules,n):
    for i in range(n):
        newString = ""
        for ch in axiom:
            newString = newString + rules.get(ch,ch)  
        axiom = newString
    return axiom

def drawLS(aTurtle,instructions,angle,distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        else:
            print('Error: %s is an unknown command'%cmd)
        
fred = turtle.Turtle()
win = turtle.Screen()

fred.up()
fred.backward(300)
fred.down()

axiom = 'F'
myRules = {'F':'F-F++F-F'}

res = applyProduction(axiom, myRules, 3)
print(res)
#drawLS(fred, "F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F", 60, 50)
drawLS(fred,res,60,20)
win.exitonclick()