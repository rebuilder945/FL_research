def maxsum(nums):
    n = len(nums)//2
    result=0
    for i range(n):
        result += min(nums[i*2],nums[i*2+1])
    return result




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

