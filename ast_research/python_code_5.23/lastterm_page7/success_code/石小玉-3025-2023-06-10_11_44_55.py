nums=input().split(" ")
nums.sort()
m=[]
for x in nums:
    i=nums.count(x)
    m.append(i)
z=0
for x in nums:
    if nums.count(x)==max(m) and z==0:        
        print(x,max(m))
    else:
        pass

