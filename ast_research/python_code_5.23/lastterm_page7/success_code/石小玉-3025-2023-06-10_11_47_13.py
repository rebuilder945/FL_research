nums=input().split(" ")
nums.sort()
m=[]
for x in nums:
    i=nums.count(x)
    m.append(i)
z=0
for x in nums:
    if nums.count(x)==max(m):        
        z=1
        k=max(m)
        v=x
    else:
        pass

if z==0:
    print(v,k)
else:
    pass

