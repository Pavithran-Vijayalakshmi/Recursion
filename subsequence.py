def subs(ind,given,arr):
    if ind == len(given):
        for i in arr:
            print(i,end = " ")
        print()
        return
    if len(arr) == 0:
        print("{}")
        return
    arr.append(given[ind])
    subs(ind+1,given,arr)
    arr.pop()
    subs(ind+1,given,arr)

arr = [3,1,2]
subs(0,arr,[])   
    