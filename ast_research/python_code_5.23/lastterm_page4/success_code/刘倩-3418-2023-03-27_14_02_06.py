def maxsum(nums):
    sorted_nums = sorted(nums)
    return sum(sorted_nums[::2])




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

