def maxsum(nums):
   nums.sort()
   a=[]
   for i in range(0,len(nums),2):
      a_sum=nums[i]+nums[i+1]
      a.append(a_sum)
      maxsum(nums)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

