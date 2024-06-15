def maxsum(nums):

    nums.sort()

    max_sum = 0

    for i in range(0, len(nums), 2):
        max_sum += nums[i]
    
    return max_sum





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

