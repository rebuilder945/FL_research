def maxsum(nums):
    nums.sort()
    minr=nums[::2]
    sumv= sum(minr)
    return sumv




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

