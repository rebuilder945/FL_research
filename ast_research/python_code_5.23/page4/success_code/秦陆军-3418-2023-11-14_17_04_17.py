def maxsum(nums):
   sum_1 = 0
   nums.sort()
   a = len(nums)
   for i in range(int(a/2)):
      sum_1 += nums[i*2-1]
      return sum_1




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

