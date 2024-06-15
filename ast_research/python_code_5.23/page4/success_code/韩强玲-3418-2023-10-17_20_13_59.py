def maxsum(y):
    y.sort(reverse = True)
    x = y[1::2]
    a = sum(x)
    return a




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

