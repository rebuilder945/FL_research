def maxsum(l):
    b=len(l)
    a=sum(sorted(l)[0:b:2])
    return a




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

