def calDegrees(nums):
      b = []
      for x in nums:
          b.append(nums.count(x))
      a = max(b)
      return a


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

