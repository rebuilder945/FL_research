def maxsum(nums):
    nums.sort()
    for i in nums:
        ls=nums[0:len(nums)+1:2]
    return sum(ls)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

