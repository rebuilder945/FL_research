n=eval(input())
m=False
t=0
if n<=99:
    print("none")
else:
    for i in range(100,n+1):
        if i<1000:
            for x in str(i):
                t+=int(x)**3
            if t==i:
                print(i)                    
                m=1
    if m==0:
        print("none")
    
