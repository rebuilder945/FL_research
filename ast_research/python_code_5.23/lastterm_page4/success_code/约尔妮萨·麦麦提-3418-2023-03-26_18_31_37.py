def maxsum(nums):    
  nums.sort()
  a=nums[0::2]
  d=sum(a)
  return d




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

