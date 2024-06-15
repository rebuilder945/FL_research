names=list(input().split(","))
nums=eval(input())
n=len(nums)
lst=[]
for i in range(n):
    tmp=[names[i],nums[i]]
    lst.append(tmp)
print(lst)
