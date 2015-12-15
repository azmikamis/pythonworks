def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",alist)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap] 
            position = position-gap

        alist[position]=currentvalue

def myshellsort(A):
    gap = len(A) // 2
    while gap > 0:
        for index in range(gap):
            for i in range(index+gap, len(A), gap):
                currval = A[i]
                position = i
                
                while position >= gap and A[position-gap] > currval:
                    A[position] = A[position-gap]
                    position -= gap
                    
                A[position] = currval
        gap //= 2
            
alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)
alist2 = [54,26,93,17,77,31,44,55,20]
myshellsort(alist2)
print(alist2)