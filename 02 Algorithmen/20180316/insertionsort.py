L = [1,26,93,17,77,31,2,44,55,20]

def insertionSort(L):
   for i in range(0,len(L)):
     min = L[i]
     while i>0 and L[i-1]>min:
         L[i]=L[i-1]
         i = i-1
     L[i]=min

insertionSort(L)
print(L)
