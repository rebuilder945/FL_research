nums = input().split(',')
n, m = map(int, input().split(','))
if n < 0 or n >= len(nums):
    print('error')
else:
    num = nums[n]
    nums.extend([num] * m)
    print(nums)
