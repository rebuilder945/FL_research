def maxsum(n):
      nums.sort()
      n=0
      for i in nums[0:-1:2]:
            n+=i
      return n
      




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

