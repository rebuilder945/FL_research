n=int(input())
ls=[x for x in range(1,n+1)]
a=ls[0]
for n in range(0,len(ls)-1):
    ls[n]=ls[n+1]
ls1=ls+ls[0]
print(ls1)
