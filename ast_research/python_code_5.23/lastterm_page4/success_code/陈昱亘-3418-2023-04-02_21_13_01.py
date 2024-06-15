def maxsum(a):
    a.sort()
    i=0
    b=0
    while i<=len(a)-2:
        b+=a[i]
        i+=2
    return b




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

