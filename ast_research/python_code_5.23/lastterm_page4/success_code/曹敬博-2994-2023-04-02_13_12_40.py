s=list(map(int,input().split(',')))
n,m=eval(input())
if n >=len(s) or n<-len(s):
    print("error")
elif  n <len(s)and n>0:
     for i in range(m):
        s.append(s[n])
     print(s)
else:
    n=n+len(s)
    for i in range(m):
         s.append(s[n])
    print(s)
       


