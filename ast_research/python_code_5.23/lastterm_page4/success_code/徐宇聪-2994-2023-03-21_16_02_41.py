nums = input().split(',')
n, m = map(int, input().split(','))
num = nums[n]
nums.extend([num] * m)
nums = [ int(x) for x in nums ]
print(nums)
