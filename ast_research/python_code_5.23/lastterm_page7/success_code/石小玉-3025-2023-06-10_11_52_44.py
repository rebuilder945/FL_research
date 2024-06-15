nums=input().split(" ")
nums.sort()
m=[]
n=[]
for x in nums:
    i=nums.count(x)
    m.append(i)
    n.append(x,i)
n=dict[n]
for k,v in n.items():
    if v==max(m):
        print(k,v)


