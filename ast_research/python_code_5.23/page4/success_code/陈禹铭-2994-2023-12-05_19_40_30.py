nums = input().split()
n, m = map(int, input().split(','))
nums=[int(i) for i in nums]
if abs(n) < len(nums):
    a=str(nums[n])
    a=eval(a)
    nums.extend(a * m)
    print(nums)
else:
    print("error")




