def maxsum(nums):
    nums.reverse()
    total = sum(nums[0::2])
    return total

nums = eval(input())
v = maxsum(nums)  # sum.nums是无效的Python语法，应该使用sum(nums)来调用函数
