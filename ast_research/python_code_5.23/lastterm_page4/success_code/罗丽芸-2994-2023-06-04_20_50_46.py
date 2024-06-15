ls=input().split(",")
n,m=eval(input())
if n<-len(ls) or n>len(ls):
    print("error")
else:
    a=ls[n]
    ls1=a*m
print(ls+ls1)
