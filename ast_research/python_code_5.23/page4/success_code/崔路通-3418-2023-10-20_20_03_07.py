def maxsum(a):
    a.sort()
    c=0
    b=0
    for x in range(len(a)):
        if  b%2==0:
            c=c+a[b]
    b+=1
    return c
    




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

