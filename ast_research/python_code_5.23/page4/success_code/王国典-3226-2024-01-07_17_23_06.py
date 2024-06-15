def search(ls):
    a=n//2
    kong=[]
    for x in ls:
        b=ls.count(x)
    if  b>a:
        kong.append(x)
    return kong





nums = eval(input())
y = search(nums)
print(y)


