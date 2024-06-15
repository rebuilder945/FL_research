def calDegrees(nums):
   degree=0
   for number in nums:
      if nums.count(number)>degree:
         degree=nums.count(number)
return degree


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

