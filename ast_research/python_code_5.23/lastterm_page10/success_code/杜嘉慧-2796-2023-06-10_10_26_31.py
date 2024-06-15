a=str(input())
b=str(input())
la=len(a)
lb=len(b)
mmax=0
for i in range(la):
    for j in range(la-i):
        s=a[i,i+j+1]
        if s in b and len(s)>mmax:
            print(s)
