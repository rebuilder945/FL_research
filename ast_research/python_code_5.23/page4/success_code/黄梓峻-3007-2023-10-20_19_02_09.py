nums=eval(input())
nums=[]
n,m=map(int,input().split(','))
if n<1 or n>m or m>len(nums):
    print("error");
else:
    del nums[n:m]
    print(nums)
