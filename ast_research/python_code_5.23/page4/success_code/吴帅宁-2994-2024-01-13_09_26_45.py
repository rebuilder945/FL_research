ls=list(eval(input()))
n,m=eval(input())
if -len(ls)<n<len(ls)+1:
    ls=ls+[ls[n]]*m
    print(ls)
else:
    print("error")

