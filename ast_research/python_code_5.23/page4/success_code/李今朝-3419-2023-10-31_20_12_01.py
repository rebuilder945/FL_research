import collections
def calDegrees(nums):
    counter = collections.Counter(nums)
    m = max(counter.values())
    return m


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

