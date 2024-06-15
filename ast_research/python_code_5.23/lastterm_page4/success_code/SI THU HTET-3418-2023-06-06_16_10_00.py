def maxsum(nums):
    nums.sort()
    min_sum=0
    for i in range(0,len(nums),2):
        min_sum += nums[i]
    return min_sum





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

