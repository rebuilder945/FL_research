def maxsum(a):
    a=list(a)
    a.sort()
    b=a[0::2]
    c=0
    for i in b:
        c+=i
    return(c)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

