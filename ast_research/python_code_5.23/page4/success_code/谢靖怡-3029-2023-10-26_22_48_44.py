names=input()
nums=input()
for i in range(len(names)):
    a=list(names[i])
for x in range(len(nums)):
    b=list(nums[x])
for r in range(len(names)):
    s=[]
    s.append(list(a[r],b[r]))
print(s)
