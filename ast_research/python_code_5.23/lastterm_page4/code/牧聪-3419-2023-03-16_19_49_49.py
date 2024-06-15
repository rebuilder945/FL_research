def calDegrees(nums):
from collections import Counter
counts = Counter(nums)
degree = max(counts.values())
return degree
      


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

