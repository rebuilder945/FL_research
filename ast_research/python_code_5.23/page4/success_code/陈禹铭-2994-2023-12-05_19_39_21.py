nums = input().split()
n, m = map(int, input().split(','))
if abs(n) < len(nums):
    nums=[int(i) for i in nums]
    a=str(nums[n])
    a=eval(a)
    nums.extend(a * m)
    print(nums)
else:
    print("error")




