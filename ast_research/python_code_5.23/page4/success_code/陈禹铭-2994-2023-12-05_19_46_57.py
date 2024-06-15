nums = input().split(',')
n, m = map(int, input().split(','))
nums=[int(i) for i in nums]
if abs(n) < len(nums):
    a=str(nums[n-1])
    nums.extend(a * m)
    nums=[int(i) for i in nums]
    print(nums)
else:
    print("error")




