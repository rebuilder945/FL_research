def maxsum(nums):
 nums.sort()
 nums=[x for x in range(1,len(nums),2)]
 v = sum(nums) 
 return(v)





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

