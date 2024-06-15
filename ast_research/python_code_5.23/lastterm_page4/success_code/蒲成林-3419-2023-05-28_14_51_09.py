from collections import Counter

def calDegrees(nums):
  
  counter = Counter(nums)
  
  degree = max(counter.values())
  return degree


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

