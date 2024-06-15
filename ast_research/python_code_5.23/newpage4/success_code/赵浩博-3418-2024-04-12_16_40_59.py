def maxsum(nums):
   nums.sort()
   sum1=sum(nums[0::2])
   return sum1




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

