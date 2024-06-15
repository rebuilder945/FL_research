nums  =  eval(input())
def maxsum(nums):
nums.sort()
return sum([nums[i] for i in range(o,len(nums),2)])




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

