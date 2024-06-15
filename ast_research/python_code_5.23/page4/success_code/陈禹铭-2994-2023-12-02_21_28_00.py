nums = eval(input())
n, m = map(int, input().split(','))
if abs(n) < len(nums):
    nums=list(nums)
    a=str(nums[n])
    a=eval(a)
    nums.extend(a * m)
    print(nums)
else:
    print("error")


