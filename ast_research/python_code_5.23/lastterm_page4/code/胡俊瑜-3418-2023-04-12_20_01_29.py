def maxsum(nums):
nums.sort()
return sum([nums[i]for i in range(0,len(nums),2)])




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

