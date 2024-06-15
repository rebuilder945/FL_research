from collections import Counter

def calDegrees(nums):
    count=Count(nums)
    d=max(count.values())
    return d


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

