def maxsum(a):
    a.sort()
    b=[]
    for i in range(a[::2]):
        b.append(i)
    c=sum(b)
    return(c)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

