def calDegrees(nums):
      a = Counter(nums)
      max_a = max(a.values())
      return max_a
      


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

