n=int(input())
lst1=[]
lst2=[]
a,b=0,1
c,d=1,2
lst3=[]
for i in range(1,n+1):
    a,b=b,a+b
    lst1.append(a)
for i in range(1,n+1):
    c,d=d,c+d
    lst2.append(c)
del lst1[0]
for i in range(0,n):
    lst3.append(lst2[i]/lst1[i])
print('%.4f'%(sum(lst3)))
