s=list(map(int,input().split(',')))
n,m=eval(input())
if n >=len(s) or n<-len(s):
    print("error")
elif  n <len(s)and n>0:
     for i in range(m):
        s.append(s[n])
     print(s)
else:
    for i in range(m):
         n=n-1
         s.append(s[-abs(n)])
    print(s)
       


