def binarysearch(A, key):
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
    
alist1 = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarysearch(alist1, 3))
print(binarysearch(alist1, 13))