ls=list(map(int,input().split(",")))
n,m=eval(input())
if n<-len(ls) or n>=len(ls):
    print("error")
else:
    ls1=[ls[n]]
    a=list(ls1)
    b=a*m
    print(ls+ls1)
