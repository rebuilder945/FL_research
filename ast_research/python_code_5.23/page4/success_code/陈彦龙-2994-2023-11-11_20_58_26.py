ls1=list(eval(input()))
n,m=eval(input())
if n<len(ls1):
    ls2=[ls1[n]]*m
    ls3=ls1+ls2
    print(ls3)
else:
    print("error")
