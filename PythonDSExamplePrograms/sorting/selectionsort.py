def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

def myselectionsort(A):
    for j in range(len(A)):
        imin = j
        for i in range(j+1,len(A)):
            if A[i] < A[imin]:
                imin = i
        if imin != j:
            A[j], A[imin] = A[imin], A[j]

            
alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)
alist2 = [54,26,93,17,77,31,44,55,20]
myselectionsort(alist2)
print(alist2)