def repeat_and_move(nums, n, m):
    if n < -len(nums) or n >= len(nums):
        return "error"
    else:
        num = nums[n]
        nums += [num] * m
        nums = nums[:n] + nums[n+m:]
        return nums
nums=eval(input())
n,m=eval(input())
print(repeat_and_move(nums, n, m))
