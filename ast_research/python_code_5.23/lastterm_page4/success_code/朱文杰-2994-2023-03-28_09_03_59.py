nums=list(eval(input()))
n,m=eval(input())
m>0
if n>0 and n>=len(nums):
    print("error")
elif n<0 and abs(n)>len(nums):
    print("error")
else:
    temp=[nums[n]]*m
    nums=nums+temp
    print(nums)
