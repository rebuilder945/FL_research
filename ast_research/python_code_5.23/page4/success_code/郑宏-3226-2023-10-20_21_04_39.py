def seach(x):
    a=len(x)//2
    c=[]
    for i in range(len(x)):
        b=x.count(x[i])
        if b>a:
            c.append(x[i])
        else:
            continue
    return(c)





nums = eval(input())
y = search(nums)
print(y)


