def calDegrees (x):
    import collections
    x=Counter(x)
    d=max(x.values)
    return (d)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

