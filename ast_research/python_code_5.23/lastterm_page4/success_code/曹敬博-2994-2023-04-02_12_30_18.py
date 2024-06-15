s=list(map(int,input().split(',')))
n,m=eval(input())
if n >=len(s) or n<-len(s):
    print("error")
else:
    for n in range(m):
        s.append(s[n])
    print(s)
