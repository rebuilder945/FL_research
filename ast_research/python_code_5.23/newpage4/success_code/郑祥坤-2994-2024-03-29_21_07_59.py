a=list(eval(input()))
n,m=eval(input())
l=len(a)
if n >=l or n <-1*l:
    print("error")
else:
    b=[a[n]]*m
    print(a+b)
