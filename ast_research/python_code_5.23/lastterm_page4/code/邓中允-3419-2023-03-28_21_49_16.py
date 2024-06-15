def calDegrees(nums)：
    a= counter(nums)
    max_freq = max(a.values())
    return max_freq


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

