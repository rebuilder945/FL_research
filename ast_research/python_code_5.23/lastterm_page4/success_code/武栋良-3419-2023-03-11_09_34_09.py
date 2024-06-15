def calDegrees(nums):
      x = max(nums.count())
      y = nums.count(x)
      return y


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

