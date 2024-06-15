def maxsum(nums):
 sum=0
 nums.sort
 n=len(nums)
 nums2=nums[:n] 
 for i in range(1,n+1):
  sum+=nums2[i]   
 return sum;     




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

