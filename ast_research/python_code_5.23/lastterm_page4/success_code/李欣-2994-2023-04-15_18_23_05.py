ls1=eval(list(input()))
n,m=input().split()
n=int(n)
m=int(m)
a=ls1[n]
while ls1.count(a)<m:
    ls1.append(a)
print(ls1)
