def maxsum(nums):
    nums.sort()
    n = len(nums) // 2
    result = 0
    for i in range(0, len(nums), 2):
        result += nums[i] 
    return result




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

