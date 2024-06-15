s=list(map(int,input().split(',')))
n,m=eval(input())
if n >=len(s) or n<-len(s):
    print("error:index out of range")
else:
    for i in range(m):
        s.append(s[n])
    print(s)
