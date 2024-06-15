def maxsum(nums):
  nums.sort()
  for i in range(0,len(nums),2):
    sum=sum+nums[i]
    return sum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

