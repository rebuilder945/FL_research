def maxsum(nums):
 nums.sort()
 for nums in range(1,len(nums),2):
  s = nums
 v = sum(s) 
 return(v)





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

