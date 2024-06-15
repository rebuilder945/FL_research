nums = eval(input())
n, m = map(int, input().split(','))
if abs(n) <= len(nums):
    element = nums[n - 1] if n > 0 else nums[n]
    nums += [element] * m
    print(nums)
else:
    print("error")

