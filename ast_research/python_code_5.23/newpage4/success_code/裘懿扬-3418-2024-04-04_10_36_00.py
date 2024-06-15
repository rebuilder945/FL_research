def maxsum(x):
    a=[]
    n=len(x)//2
    for i in range(0,n):
        b=max(x)
        x.remove(b)
        c=max(x)
        a.append(c)
        x.remove(c)
    return sum(a)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

