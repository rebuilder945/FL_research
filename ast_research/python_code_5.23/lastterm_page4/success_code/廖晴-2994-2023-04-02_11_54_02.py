s=list(map(int,input().split(',')))
n,m=eval(input())
if n >=len(s) or n<-len(s):
    print("error")
else:
    a=s[n]
    for i in range(m):
        s.append(a)
    print(s)
