n=int(input())
m=False
t=0
if n<=99:
    print("none")
else:
    for i in range(100,n+1):
        t+=(n%10)**3
        n=n//10
        if t==i:
                print(i)                    
                m=1
    if m==0:
        print("none")
    
