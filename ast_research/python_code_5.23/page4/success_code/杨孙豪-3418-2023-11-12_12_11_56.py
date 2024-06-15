def maxsum(x):
    x.sort()
    min=x[::2]
    return(sum(min))




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

