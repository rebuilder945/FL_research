n=int(input())
m=False
t=0
if n<=99:
    print("none")
else:
    for i in range(100,n+1):
        while i !=0:
            
            t+=(i%10)**3
            i=i//10
            if t==i:
                print(i)                    
                m=1
    if m==0:
        print("none")
    
