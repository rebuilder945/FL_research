def maxsum(x):
    x.sort()
    a=x[-1]+x[-2]
    print(a)





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

