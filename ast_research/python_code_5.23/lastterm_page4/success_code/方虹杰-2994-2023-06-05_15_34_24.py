a=input().split(",")
n,m=eval(input())
if n>=len(a) or n<-len(a):
    print("error")
else:
    a+=a[n]*m

    print(list(map(int,a)))
