a=list(eval(input()))
n,m=eval(input())
if n >=len(a) or n<-1*len(a):
    print("error")
else:
    b=[a[n]]*m
    a=a+b
    print(a)
