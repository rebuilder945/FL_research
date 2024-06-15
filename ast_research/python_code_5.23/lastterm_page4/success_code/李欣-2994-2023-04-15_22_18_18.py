ls1=input().split(',')
n,m=input().split(',')
n=int(n)
m=int(m)
a=ls1[n]
while ls1.count(a)<m+1:
    ls1.append(a)
ls2=list(map(int,ls1))
print(ls2)
