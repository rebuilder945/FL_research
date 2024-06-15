nums = input().split()
n, m = map(int, input().split(','))
if abs(n) < len(nums):
    nums.extend(nums[n] * m)
    nums=[int(i) for i in nums]
    print(nums)
else:
    print("error")






