def calDegrees(nums)：
    count = count(nums)
    max_freq = max(count.values())
    return max_freq


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

