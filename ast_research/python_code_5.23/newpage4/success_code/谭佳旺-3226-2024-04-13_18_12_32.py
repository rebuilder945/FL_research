def search(a):
    b=[]
    if len(a)==1:
        return a[0]
    for i in a:
        if a.count(i)>(len(a)/2):
            return i
    return False 





nums = eval(input())
y = search(nums)
print(y)


