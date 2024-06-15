def calDegrees(x):
    y = max(set(x))
    key = x.count(y)
    return(key)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

