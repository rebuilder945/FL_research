a=input().split(",")
n,m=eval(input())
a=list(a)
if n>len(a)-1 or n<-len(a)+1:
    print("error")
else:
    c=[a[n]]*m
    print(a+c)
