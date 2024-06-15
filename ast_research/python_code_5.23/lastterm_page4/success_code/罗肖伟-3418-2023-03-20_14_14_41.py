def maxsum(nums):
      sums=0
      nums=nums.sort()
      for i in range(0,len(nums),2):
           sums=sums+nums[i]
      return sums




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

