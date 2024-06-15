def wf(x):
    t=0
    a=x
    while x!=0:
        t+=(x%10)**3
        x=x//10
    if t==a:
            print(a)
            return True
n=int(input())
m=False
for i in range(2,n+1):
    if wf(i):
        m=1
if m==0:
    print("none")

    
