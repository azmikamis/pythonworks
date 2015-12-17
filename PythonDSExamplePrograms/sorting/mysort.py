def bubblesort(A):
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

alist1 = [54,26,93,17,77,31,44,55,20]
bubblesort(alist1)
print(alist1)

def insertionsort(A):
    for i in range(1,len(A)):
        x = A[i]
        j = i

        while j>0 and A[j-1]>x:
            A[j] = A[j-1]
            j -= 1
            
        A[j] = x

alist2 = [54,26,93,17,77,31,44,55,20]
insertionsort(alist2)
print(alist2)

def selectionsort(A):
    for j in range(len(A)):
        imin = j
        for i in range(j+1,len(A)):
            if A[i] < A[imin]:
                imin = i
        if imin != j:
            A[j], A[imin] = A[imin], A[j]

alist3 = [54,26,93,17,77,31,44,55,20]
selectionsort(alist3)
print(alist3)

def shellsort(A):
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

alist4 = [54,26,93,17,77,31,44,55,20]
shellsort(alist4)
print(alist4)

def quicksort(A):
    quicksorthelper(A,0,len(A)-1)
    
def quicksorthelper(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        quicksorthelper(A, lo, p-1)
        quicksorthelper(A, p+1, hi)        
        
def partition(A, lo, hi):
    pivot = A[hi]
    i = lo
    for j in range(lo, hi):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[hi] = A[hi], A[i]
    return i

alist5 = [54,26,93,17,77,31,44,55,20]
quicksort(alist5)
print(alist5)

def mergesort(A):
    if len(A) > 1:
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]
 
        mergesort(left)
        mergesort(right)
 
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                A[k]=left[i]
                i += 1
            else:
                A[k]=right[j]
                j += 1
            k += 1
 
        while i<len(left):
            A[k]=left[i]
            i += 1
            k += 1
 
        while j<len(right):
            A[k]=right[j]
            j += 1
            k += 1

alist6 = [54,26,93,17,77,31,44,55,20]
mergesort(alist6)
print(alist6)

def heapsort(a):
    def sift(start, count):
        root = start
 
        while root * 2 + 1 < count:
            child = root * 2 + 1
            if child < count - 1 and a[child] < a[child + 1]:
                child += 1
            if a[root] < a[child]:
                a[root], a[child] = a[child], a[root]
                root = child
            else:
                return
 
    count = len(a)
    start = count / 2 - 1
    end = count - 1
 
    while start >= 0:
        sift(start, count)
        start -= 1
 
    while end > 0:
        a[end], a[0] = a[0], a[end]
        sift(0, end)
        end -= 1
 
alist7 = [54,26,93,17,77,31,44,55,20]
heapsort(alist7)
print(alist7)