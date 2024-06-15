ls=list(eval(input()))
n,m=eval(input())
if 0<n<len(ls):
    ls=ls+[ls[n]]*m
    print(ls)
else:
    print("error")

