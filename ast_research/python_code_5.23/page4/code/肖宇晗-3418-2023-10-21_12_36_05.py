def maxsum(nums):
       for a,b in nums:
             n=a+b
             m = max(n)
      return m




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

