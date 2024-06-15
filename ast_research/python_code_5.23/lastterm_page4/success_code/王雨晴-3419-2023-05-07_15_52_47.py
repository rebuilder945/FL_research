def calDegrees(y):
    n=[y.count(x) for x in set(y)]
    return max(n)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

