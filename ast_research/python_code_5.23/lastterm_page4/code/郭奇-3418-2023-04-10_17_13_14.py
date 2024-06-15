def maxsum(nums):
    n = len(nums)
    result=0
    for i range(n):
        for j in range(i+1,n):
            result = max(result,nums[i]+nums[j])
    return result




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

