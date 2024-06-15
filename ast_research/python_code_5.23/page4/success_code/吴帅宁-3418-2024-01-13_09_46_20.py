def maxsum(nums):
    nums.sort()
    min1=min(nums)
    max1=nums[len(nums)-2]
    return min1+max1





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

