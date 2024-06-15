x=list(map(int,input().split(",")))
n,m=eval(input())
if n<-len(x) or n>=len(x):
    print("error")
else:
    y=[x[n] for i in range(m)]
    print(x+y)
