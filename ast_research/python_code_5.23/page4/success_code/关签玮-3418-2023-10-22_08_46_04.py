def maxsum(a):
    a.sort()
    b=len(a)
    c=[]
    for i in a[0:b:2]:
        c.append(i)
    sum(c)
    return(sum(c))




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

