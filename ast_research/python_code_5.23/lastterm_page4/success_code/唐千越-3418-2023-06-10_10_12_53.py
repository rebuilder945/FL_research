def maxsum(nums):
      b=0
      l = len(nums)
      nums.sort(reverse=False)
      for i in range(l):
            if i%2 == 0:
                b += nums[i]
      return b
                




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

