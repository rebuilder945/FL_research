a=list(eval(input()))
n,m=eval(input())
if n>=len(a) or n<-len(a):
    print('error')
else:
    b=[a[n]]*m
    print(a+b)

