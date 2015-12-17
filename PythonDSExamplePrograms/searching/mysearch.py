def mybinarysearch(A, key):
    imin = 0
    imax = len(A)-1
    
    while imin <= imax:
        imid = (imin+imax) // 2
        if A[imid] == key:
            return True
        elif A[imid] < key:
            imin = imid+1
        else:
            imax = imid-1
            
    return False
    
testlist2 = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(mybinarysearch(testlist2, 3))
print(mybinarysearch(testlist2, 13))