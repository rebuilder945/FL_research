def maxsum(nums):
    nums.sort()
    a=int(nums[0])+int(nums[len(nums)/2])
    return a




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

