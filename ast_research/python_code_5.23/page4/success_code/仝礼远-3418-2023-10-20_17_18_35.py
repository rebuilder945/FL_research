def maxsum(nums):
    nums.sort()
    n=nums[::2]
    return sum(n)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

