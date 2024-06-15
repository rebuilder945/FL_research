n=int(input())
l=[a for a in range(1,n+1)]
l1=l.copy()
for i in range(len(l)-1):
    l1[i]=l[i+1]
l1[-1]=l[0]
print(l1)
