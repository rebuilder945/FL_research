ls1=input().split(' ')
n,m=map(int,input().split(' '))
#print(ls1)
#print(n,m)
a=ls1[m]
ls1[m]=ls1[n]
ls1[n]=a
print(ls1)
