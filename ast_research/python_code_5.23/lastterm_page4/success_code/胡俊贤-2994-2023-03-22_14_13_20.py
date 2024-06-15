l=input()
nums=[]
num=l.split(',')
for i in num:
    nums.append(int(i))
n,m=eval(input())
l=len(nums)
if -l<=n<l:
    x=nums[n]
    for i in range(m):
        nums.append(x)
    print(nums)
else:
    print('error')
