nums = eval(input())
n, m = map(int, input().split(','))
if abs(n) < len(nums):
    
    nums.extend(nums[n] * m)
    print(nums)
else:
    print("error")


