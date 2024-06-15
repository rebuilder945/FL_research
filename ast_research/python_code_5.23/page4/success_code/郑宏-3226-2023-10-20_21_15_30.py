def search(x):
    e=[]
    a=len(x)
    b=a//2
    for i in range(a):
        c=x[i]
        if c>b:
            e.append(c)
        else:
            continue
    e=list(set(e))
    return(e)





nums = eval(input())
y = search(nums)
print(y)


