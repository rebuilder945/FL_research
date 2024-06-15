def maxsum(nums):
   nums.sort()
   max = nums[-1] + nums[-2]
   min = nums[0] + nums[1]
   sum = max+min
   return sum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

