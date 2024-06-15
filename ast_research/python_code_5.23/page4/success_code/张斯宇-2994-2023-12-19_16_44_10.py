lst=[int(i) for i in input().split(',')]

n,m=eval(input())

if(n>=len(lst) or n<-len(lst)):
    print("error")
else:
    ans=lst+[lst[n]]*m
    print(ans)
