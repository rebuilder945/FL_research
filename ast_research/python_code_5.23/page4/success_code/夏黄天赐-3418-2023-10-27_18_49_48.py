def maxsum(nums):
    a=len(nums)
    nums.sort()
    ls=nums[0:a:2]
    return sum(ls)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

