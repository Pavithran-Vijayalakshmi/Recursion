def qs(l:int , h:int,arr):
    if l>=h:
        return
    partition = quickSort(l,h,arr)
    qs(l,partition-1,arr)
    qs(partition+1,h,arr)


def quickSort(l,h,arr):
    pivot = arr[l]
    i = l
    j = h
    while(j>i):
        while(arr[i]<=pivot and i<=h):
            i+=1
        while(arr[j]>pivot and j>=i):
            j-=1
        if(i<j):
            arr[i],arr[j] = arr[j],arr[i]
    arr[l],arr[j] = arr[j],pivot
    return j

arr = [4,6,1,5,3,2,7]
qs(0,len(arr)-1,arr)
print(arr)
    