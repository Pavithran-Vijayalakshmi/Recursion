def subs(ind,given,arr,s,ds):
    if ind == len(given):
        ds.append(sum(arr))
        return
    
    arr.append(given[ind])
    subs(ind+1,given,arr,s,ds)
    
    arr.pop()
    subs(ind+1,given,arr,s,ds)
    return ds.sort()

arr = [1,2,3]
a = subs(0,arr,[],0,[])
a.so
    