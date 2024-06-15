nums = eval(input())
n, m = map(int, input().split(','))
if 0 <= abs(n) <= len(nums):
    element = nums[n] if n >= 0 else nums[n + len(nums)]
    nums.extend([element] * m)
    print(nums)
else:
    print("error")

