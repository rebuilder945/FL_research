def maxsum(nums):
    nums.sort()
    x=nums[0:-1:2]
    return sum(x)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

