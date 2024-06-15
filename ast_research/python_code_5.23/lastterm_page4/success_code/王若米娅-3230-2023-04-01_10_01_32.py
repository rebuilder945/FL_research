lst=[3,3,4,2,1,0]
lst.sort()
lst2=[]
for i in range(len(lst)):
    a=lst[i]*10**i
    lst2.append(a)
c=sum(lst2)
print(c)
