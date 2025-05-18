def subs(i,arr,ds,k):
    if i==len(arr):
        if sum(ds) == k:
            print(ds)
            return True
        return False

    ds.append(arr[i])
    if subs(i+1,arr,ds,k) == True:
        return True
    ds.pop()
    if subs(i+1,arr,ds,k) == True:
        return True
    return False
    
arr= [ 1,2,1,3,4,1,2,5]
k = 5
subs(0,arr,[],k)