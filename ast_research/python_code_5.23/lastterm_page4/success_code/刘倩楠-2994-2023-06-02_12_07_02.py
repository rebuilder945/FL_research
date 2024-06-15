nums=input().split(",")
n,m=eval(input())
ls=[]
if n>=len(nums) or n<=-len(nums):
    print("error")
else:
    for i in list(range(len(nums))):
        ls.append(nums[i])
ls.extend(nums[n]*m)
lt=[]
for item in ls:
    lt.append(int(item))
print(lt)
