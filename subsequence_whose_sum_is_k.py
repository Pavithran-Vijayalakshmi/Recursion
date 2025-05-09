def subs(i,arr,ds,k):
    if i>=len(arr):
        if sum(ds) == k:
            print(ds)
        return

    ds.append(arr[i])
    subs(i+1,arr,ds,k)
    ds.pop()
    subs(i+1,arr,ds,k)
    
arr= [ 1,2,1,3,4,2,3]
k = 5
subs(0,arr,[],k)