n=int(input())
lst1=[]
lst2=[]
a,b=1,1
c,d=1,2
lst3=[]
for i in range(1,n+1):
    a,b=b,a+b
    lst1.append(a)
for q in range(1,n+1):
    c,d=d,c+d
    lst2.append(c)

for m in range(0,n):
    lst3.append(lst2[m]/lst1[m])
print('%.4f'%(sum(lst3)))
