def maxsum(a):
    a.sort()
    b=a[-2]+a[-4]
    return b




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

