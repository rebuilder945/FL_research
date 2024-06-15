ls1=input().split(',')
n,m=input().split(',')
n=int(n)
m=int(m)
if n>=0:
    if n<len(ls1):
        a=ls1[n]
        while ls1.count(a)<m+1:
            ls1.append(a)
        ls2=list(map(int,ls1))
        print(ls2)
    else:
        print("error")
else:
    if n>=-len(ls1):
        a=ls1[n]
        while ls1.count(a)<m+1:
            ls1.append(a)
        ls2=list(map(int,ls1))
        print(ls2)
    else:
        print("error")
