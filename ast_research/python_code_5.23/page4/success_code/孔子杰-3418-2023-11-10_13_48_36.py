def maxsum(nums):
      nums.sort()
      minv=nums[::2]
      return(sum(minv))




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

