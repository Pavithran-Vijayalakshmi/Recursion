def subs(ind,given,arr,k):
    if ind == len(given):
        if k == 0:
            print(arr)
        return
    if (given[ind] <= k):
        arr.append(given[ind])
        subs(ind,given,arr,k-given[ind])
        arr.pop()
    subs(ind+1,given,arr,k)

arr = [3,1,2]
t = 3
subs(0,arr,[],t)
    