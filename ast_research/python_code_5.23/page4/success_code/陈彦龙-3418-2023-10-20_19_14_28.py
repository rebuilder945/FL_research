def maxsum(nums):
      nums.sort()
      s=0
      for i in nums[0::2]:
            s=s+i
      return(s)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

