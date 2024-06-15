n=int(input())
l1=[]
for i in range(1,n+1):
    l1.append(i)
a=l1[0]
del l1[0]
l1.append(a)
print(l1)
