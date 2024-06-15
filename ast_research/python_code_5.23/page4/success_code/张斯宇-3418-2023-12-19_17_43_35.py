def maxsum(nums):
    index=int(len(nums)/2)
    return nums[0]+nums[index]





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

