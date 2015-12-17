def mybubblesort(A):
    n = len(A)
    while True:
        swapped = False        
        for i in range(1,n):
            if A[i-1] > A[i]:
                A[i-1], A[i] = A[i], A[i-1]
                swapped = True
        n -= 1 #optimization
        if not swapped:
            break

alist = [54,26,93,17,77,31,44,55,20]
mybubblesort(alist)
print(alist)

def myinsertionsort(A):
    for i in range(1,len(A)):
        x = A[i]
        j = i

        while j>0 and A[j-1]>x:
            A[j] = A[j-1]
            j -= 1
            
        A[j] = x

alist = [54,26,93,17,77,31,44,55,20]
myinsertionsort(alist)
print(alist)

def myselectionsort(A):
    for j in range(len(A)):
        imin = j
        for i in range(j+1,len(A)):
            if A[i] < A[imin]:
                imin = i
        if imin != j:
            A[j], A[imin] = A[imin], A[j]

alist = [54,26,93,17,77,31,44,55,20]
myselectionsort(alist)
print(alist)

def myshellsort(A):
    gap = len(A) // 2
    while gap > 0:
        for i in range(gap):
            for j in range(i+gap, len(A), gap):
                x = A[j]
                p = j
                
                while p >= gap and A[p-gap] > x:
                    A[p] = A[p-gap]
                    p -= gap
                    
                A[p] = x
        gap //= 2

alist = [54,26,93,17,77,31,44,55,20]
myshellsort(alist)
print(alist)

def myquicksort(A):
    myquicksorthelper(A,0,len(A)-1)
    
def myquicksorthelper(A, lo, hi):
    if lo < hi:
        p = mypartition(A, lo, hi)
        myquicksorthelper(A, lo, p-1)
        myquicksorthelper(A, p+1, hi)        
        
def mypartition(A, lo, hi):
    pivot = A[hi]
    i = lo
    for j in range(lo, hi):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[hi] = A[hi], A[i]
    return i

alist = [54,26,93,17,77,31,44,55,20]
myquicksort(alist)
print(alist)
