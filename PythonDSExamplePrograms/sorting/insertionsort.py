def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

def myinsertionsort(A):
    for i in range(1,len(A)):
        x = A[i]
        j = i

        while j>0 and A[j-1]>x:
            A[j] = A[j-1]
            j -= 1
            
        A[j] = x
        
alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print alist
alist2 = [54,26,93,17,77,31,44,55,20]
myinsertionsort(alist2)
print(alist2)