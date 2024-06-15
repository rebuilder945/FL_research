nums = list(map(int,input().split(',')))
n,m = eval(input())
if n < 0 or n >= len(nums):
    print('error')
else:
    num = nums[n]
    for x in range(m):
        nums.append(num)
        x = x+1
    print(nums)
