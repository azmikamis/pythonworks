def frequencyTableAlt(alist):
    print("ITEM","FREQUENCY")
    slist = alist[:]
    slist.sort()
    
    countlist = [ ]
    
    previous = slist[0]
    groupCount = 0
    for current in slist:
        if current == previous:
            groupCount = groupCount + 1
            previous = current
        else:
            print(previous, "   ", groupCount)
            previous = current
            groupCount = 1

    print(current, "   ", groupCount)
    
frequencyTableAlt([4,4,4,4,4,4,4,4,4,4,4,4,4])
