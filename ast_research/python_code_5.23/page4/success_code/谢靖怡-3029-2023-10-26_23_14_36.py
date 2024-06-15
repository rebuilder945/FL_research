names=input()
nums=input()
for i in range(len(names)):
    a=list(names[i])
for x in range(len(nums)):
    b=list(nums[x])
for r in range(len(names)):
    s=[]
    s.append(list(a[r]))
    s.append(list(b[r]))
print(s)
