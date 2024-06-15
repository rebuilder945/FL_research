nums = eval(input())
n,m = map(int,input().split(','))
if n <= len(nums):    
    b = []
    for x in range(n):
        b.append(nums[x])
    for i in range(m,len(nums)):
        b.append(nums[i])
    print(b)
else:
    print('error')

