def maxsum(nums):
      nums.sort()
      return nums[0]+nums[2]




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

