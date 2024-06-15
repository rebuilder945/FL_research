a=list(map(int,input().split(",")))
n,m=eval(input())
if n<-len(a) or n>=len(a):
    print("error")
else:
    for i in range(m):
        a.append(a[n])
    print(a)
