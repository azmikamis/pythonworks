import turtle
def frequencyChart(alist):

    countdict = {}      

    for item in alist:
        if item in countdict:
            countdict[item] = countdict[item]+1
        else:
            countdict[item] = 1         
    
    itemlist = list(countdict.keys())
    minitem = 0
    maxitem = len(itemlist)-1
    
    countlist = countdict.values()
    maxcount = max(countlist)
    
    wn = turtle.Screen()
    chartT = turtle.Turtle()
    wn.setworldcoordinates(-1,-1,maxitem+1,maxcount+1)
    chartT.hideturtle()
    
    chartT.up()
    chartT.goto(0,0)
    chartT.down()
    chartT.goto(maxitem,0)
    chartT.up()
    
    chartT.goto(-1,0)
    chartT.write("0",font=("Helvetica",16,"bold"))
    chartT.goto(-1,maxcount)
    chartT.write(str(maxcount),font=("Helvetica",16,"bold"))
    
    for index in range(len(itemlist)):
        chartT.goto(index,-1)
        chartT.write(str(itemlist[index]),font=("Helvetica",16,"bold"))
        
        chartT.goto(index,0)
        chartT.down()
        chartT.goto(index,countdict[itemlist[index]])
        chartT.up()
    wn.exitonclick()


frequencyChart([3,3,5,7,1,2,5,2,3,4,6,3,4,6,3,4,5,6,6])