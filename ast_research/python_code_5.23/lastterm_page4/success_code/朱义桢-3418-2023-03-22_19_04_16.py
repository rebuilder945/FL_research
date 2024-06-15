def maxsum(nums):
      nums.sort()
      a = nums[ :len(nums)/2+1]
      b = nums[len(nums)/2+1: ]
      a1=min(a)
      a2=min(b)
      c=a1+a2
      return(c)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

