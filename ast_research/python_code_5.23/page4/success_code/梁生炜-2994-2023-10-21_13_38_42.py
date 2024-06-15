ls=list(map(int,input().split(",")))
n,m=eval(input())
a=[]
if n<=len(ls):
    a.append(ls[n])
    ls1=ls+a*m
    print(ls1)
else:
    print("error")
