def maxsum(nums):
   nums.sort()
   a=[]
   for i in nums[0::2]:
      a_sum=nums[i]+nums[i+1]
      a.append(a_sum)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

