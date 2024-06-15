ls=[0,1,2,3,2]
ls.sort()
a=[0 for x in range(0,len(ls))]
for i in range(0,len(ls)):
    a[i]=ls[i]*(10**i)
x=sum(a)
print(x)

