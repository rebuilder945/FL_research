num=list(eval(input()))
n,m=eval(input())
a=len(n)
if n>=a or n<-1*a:
    print("error")
else:
    b=[num[n]]*m
    num=num+b
    print(num)
