from collections import Counter
def calDegrees(nums):
     count=Counter(nums)
     calDegress=max(count.values)
     return calDegress


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

