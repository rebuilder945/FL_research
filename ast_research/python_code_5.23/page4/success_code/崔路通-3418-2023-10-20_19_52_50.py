def maxsum(a):
    a.sort()
    c=[]
    for x in range(len(a)):
        b=0
        if  not (b+3)%2:
            c.append(a[b])
    return sum(c)
    




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

