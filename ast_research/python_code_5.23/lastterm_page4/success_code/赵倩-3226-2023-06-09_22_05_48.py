def search(x):
    l=[]
    for i in x:
        if x.count(i)>(len(x)/2) and i not in l:
            l.append(i)
            return i
    if len(l)==0:
        return "False"





nums = eval(input())
y = search(nums)
print(y)


