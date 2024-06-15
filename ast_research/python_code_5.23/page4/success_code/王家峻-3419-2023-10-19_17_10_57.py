def calDegrees(nums):
      x=0
      for y in nums:
           if nums.count(y)>x:
              x=nums.count(y)
      return x


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

