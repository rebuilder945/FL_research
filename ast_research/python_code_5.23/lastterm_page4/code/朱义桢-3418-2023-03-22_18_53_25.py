def maxsum(nums):
      a = nums[ :n+1]
      b = nums[n+1: ]
      c=[a+b,for x in a for y in b]
      return(max(c))




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

