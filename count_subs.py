def subs(i,arr,ds,k,count):
    if i==len(arr):
        if sum(ds) == k:
            return 1
        return 0
    ds.append(arr[i])
    left = subs(i+1,arr,ds,k,count)
    ds.pop()
    right = subs(i+1,arr,ds,k,count)
    return left + right
    
arr= [1,2,3,4,1]
k = 4
print(subs(0,arr,[],k,0))