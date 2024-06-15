def maxsum(nums):
    nums.sort()  
    min_sum = sum(nums[i] for i in range(0, len(nums), 2))  
    return min_sum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

