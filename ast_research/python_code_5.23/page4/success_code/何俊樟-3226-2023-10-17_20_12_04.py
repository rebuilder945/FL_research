def search(a):
    b=len(a)/2
    c=0
    for x in a:
        d=a.count(x)
        if d>b :
            c=x
        else:
            pass
    if c==0:
        y="False"
    else:
        y=c





nums = eval(input())
y = search(nums)
print(y)


