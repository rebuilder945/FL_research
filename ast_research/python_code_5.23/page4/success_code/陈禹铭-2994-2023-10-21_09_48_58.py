nums = eval(input())
n, m = map(int, input().split(','))
if abs(n) < len(nums):
    element = nums[n]
    nums.extend([element] * m)
    print(nums)
else:
    print("error")

