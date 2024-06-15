n=int(input())
ls=[x for x in range(1,n+1)]
a=ls[0]
for i in range(1,len(ls)):
    ls[i-1]=ls[i]
    ls[0*-1]=a
print(ls)
