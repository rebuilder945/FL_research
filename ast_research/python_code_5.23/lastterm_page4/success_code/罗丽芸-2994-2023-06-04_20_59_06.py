ls=list(map(int,input().split(",")))
n,m=eval(input())
n=int(n)
m=int(m)
if n<-len(ls) or n>=len(ls):
    print("error")
else:
    a=list(ls[n])
    ls1=a*m
print(ls+ls1)
