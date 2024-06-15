def search(x):
    for i in x:
        if x.count(i)>len(x)//2:
            a=i
        else:
            a=False
    return(a)





nums = eval(input())
y = search(nums)
print(y)


