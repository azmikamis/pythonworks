def createWordDict(dname):
    myDict = {}
    myFile = open(dname, 'r')
    for line in myFile:
        myDict[line[:-1]] = True
    return myDict

def railBreak(cipherText):
    wordDict = createWordDict('wordlist.txt')
    cipherLen = len(cipherText)
    maxGoodSoFar = 0
    bestGuess = "No words found in dictionary"
    for i in range(1,cipherLen+1):
        words = railDecrypt(cipherText,i)
        goodCount = 0
        for w in words: 
            if w in wordDict:
                goodCount = goodCount + 1
        if goodCount > maxGoodSoFar:     
            maxGoodSoFar = goodCount
            bestGuess = " ".join(words)  
    return bestGuess    

def railDecrypt(cipherText,numRails):
    railLen = len(cipherText) // numRails
    solution = ''
    for col in range(railLen):	
        for rail in range(numRails):
            nextLetter = (col + rail * railLen) 
            solution = solution + cipherText[nextLetter] 
    return solution.split()
    
print(railBreak("n oci mreidontoowp mgorw"))