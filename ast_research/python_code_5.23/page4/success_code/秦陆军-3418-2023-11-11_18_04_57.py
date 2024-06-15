def maxsum(nums):
   result = 0
   n = len(nums)//2
   nums.sort()
   for i in range(n):
        result += nums[i*2]
   return result
      




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

