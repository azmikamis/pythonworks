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
    for passnum in range(len(A)):
        indexmin = passnum
        for index in range(passnum+1,len(A)):
            if A[index] < A[indexmin]:
                indexmin = index
        
        A[passnum], A[indexmin] = A[indexmin], A[passnum]

            
alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)
alist2 = [54,26,93,17,77,31,44,55,20]
myselectionsort(alist2)
print(alist2)