nums=eval(input())
n,m=eval(input())
l=len(nums)
if -l<=n<l:
    x=nums[n]
    for i in range(m):
        nums.append(x)
    print(nums)
else:
    print('error')
