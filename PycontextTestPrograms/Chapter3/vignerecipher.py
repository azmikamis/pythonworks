def encryptVignere(key,plainText):
    cipherText = ""
    keyLen = len(key)
    charNum = 0
    for i in range(len(plainText)):
        ch = plainText[i]
        if ch == ' ':
            cipherText = cipherText + ch
        else:
            cipherText = cipherText + vignereIndex(key[i%keyLen],ch)
    return cipherText

def vignereIndex(keyLetter,plainTextLetter):
        keyIndex = letterToIndex(keyLetter)
        ptIndex = letterToIndex(plainTextLetter)
        newIdx = (ptIndex + keyIndex) % 26
        return indexToLetter(newIdx)
        
def letterToIndex(ch):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    idx = alphabet.find(ch)
    if idx < 0:
        print ("error: letter not in the alphabet", ch)
    return idx

def indexToLetter(idx):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    if idx > 26:
        print ('error: ', idx, ' is too large')
        letter = ''
    elif idx < 0:
        print ('error: ', idx, ' is less  than 0')
        letter = ''
    else:
        letter = alphabet[idx]
    return letter
    
print(encryptVignere("s","t"))
