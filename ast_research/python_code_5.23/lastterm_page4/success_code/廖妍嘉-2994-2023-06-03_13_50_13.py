a = list(map(int,input().split(",")))
n,m=eval(input())
if(n<-len(a) or n>=len(a)):
    print("error")
else:
    temp = [a[n] for i in range(0,m)]
    print(a+temp)

