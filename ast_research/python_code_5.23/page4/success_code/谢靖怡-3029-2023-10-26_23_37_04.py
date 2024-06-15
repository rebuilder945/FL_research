names=input().split(",")
nums=input()
for i in range(len(names)):
    a=list(names[i])
for x in range(len(nums)):
    b=list(nums[x])
for r in range(len(names)):
    c=(a[r],b[r])
    s=[]
    s.append(list(c))
print(s)
