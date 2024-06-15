def search(a):
    b=max(a,key=a.count)
    c=0
    if b in a:
        c=c+1
    d=len(a)
    e=d/2
    if c>e:
        return b
    else :
        return "False"





nums = eval(input())
y = search(nums)
print(y)


