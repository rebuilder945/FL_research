nums=input().split(",")
n,m=eval(input())
ls=[]
if n>len(nums):
    print("error")
else:
    for i in list(range(len(nums))):
        if i!=(n):
            ls.append(nums[i])
ls.extend(nums[n]*m)
lt=[]
for item in ls:
    lt.append(int(item))
print(lt)
