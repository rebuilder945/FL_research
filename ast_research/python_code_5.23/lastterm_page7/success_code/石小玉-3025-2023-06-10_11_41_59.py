nums=input().split("")
nums.sort()
m=[]
for x in nums:
    i=nums.count(x)
    m.append(i)
for x in nums:
    if nums.count(x)==max(m):
        print(x,max(m))
    else:
        pass

