def maxsum(nums):
      nums.sort()
      a = nums[ :n+1]
      b = nums[n+1: ]
      a1=min(a)
      a2=min(b)
      c=a+b
      return(c)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

