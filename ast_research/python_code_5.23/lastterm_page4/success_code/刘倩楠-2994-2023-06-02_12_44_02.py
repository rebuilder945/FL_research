nums=input().split(",")
n,m=eval(input())
ls=[]
if n>=len(nums) or n<=-len(nums):
    print("error")
else:
    for i in list(range(len(nums))):
        ls.append(nums[i])
lt=[]
lt.append(nums[n])
temp=lt*m
lst=ls+temp
lt1=[]
for item in lst:
    lt1.append(int(item))
print(lt1)
