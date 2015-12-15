def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

def myinsertionsort(A):
    for passnum in range(1,len(A)):
        currval = A[passnum]
        index = passnum

        while index>0 and A[index-1]>currval:
            A[index] = A[index-1]
            index -= 1
            
        A[index] = currval
        
alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print alist
alist2 = [54,26,93,17,77,31,44,55,20]
myinsertionsort(alist2)
print(alist2)