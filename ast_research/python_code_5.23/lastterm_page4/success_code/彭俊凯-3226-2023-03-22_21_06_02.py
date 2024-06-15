def search(x):
    for i in range(len(x)):
       a=x.count(x[i])
       if a>len(x)//2:
         return a
    else:
        a=False
        return a





nums = eval(input())
y = search(nums)
print(y)


