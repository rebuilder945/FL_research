n=int(input())
lst=range(1,n+1)
prt=[]
top=lst[0]
for i in range(len(lst)-1):
    prt.append(lst[i+1])
prt.append(top)
print(prt)

