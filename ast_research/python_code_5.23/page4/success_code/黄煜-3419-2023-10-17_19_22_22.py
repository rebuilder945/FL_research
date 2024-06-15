from collections import Counter
def calDegrees(nums):
    count=Counter(nums)
    calDegrees=max(count.values())
    return calDegrees


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

