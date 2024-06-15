from collections import Counter
def calDegrees(nums):
      count = Counter(nums)
      a=max(count.values())
      return a
             


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

