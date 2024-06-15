def search(n):
    for x in range(0,len(n)-1,1):
        if n.count(x) >len(n)//2:
            n=x
        else:
            n="False"





nums = eval(input())
y = search(nums)
print(y)


