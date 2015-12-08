def removeMatches(myString,removeString):
    newStr = ""
    for ch in myString:
        if ch not in removeString:
            newStr = newStr + ch
    return newStr
        
def removeDupes(myString):
    newStr = ""
    for ch in myString:
        if ch not in newStr:
            newStr = newStr + ch
    return newStr
    
def letterFrequency(text):
    text = text.lower()
    nonletters = removeMatches(text,alphabet)
    nonletters = removeDupes(nonletters)
    text = removeMatches(text,nonletters)
    lcount = {}
    total = len(text)
    for ch in text:
        lcount[ch] = lcount.get(ch,0) + 1
    for ch in lcount:
        lcount[ch] = lcount[ch] / total
    return lcount
    
def getFreq(t):
    return t[1]
    
alphabet="abcdefghijklmnopqrstuvwxyz"
f = open("wells.txt","r")
text = f.read()

lf = letterFrequency(text)
print(lf)
lflist = list(lf.items())
print(lflist)
lflist.sort(key=getFreq, reverse=True)
print(lflist)

for entry in lflist:
    print("%s %5.3f"%entry)
    