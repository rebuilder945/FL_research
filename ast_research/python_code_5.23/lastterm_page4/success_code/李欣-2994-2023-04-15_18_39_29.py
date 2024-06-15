ls1=list(eval(input().split(',')))
n,m=input().split(',')
n=int(n)
m=int(m)
a=ls1[n]
while ls1.count(a)<m+1:
    ls1.append(a)
print(ls1)
