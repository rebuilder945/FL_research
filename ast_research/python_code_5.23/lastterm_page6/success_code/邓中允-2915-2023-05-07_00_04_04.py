n=eval(input())
gewei=n%10
shiwei=n//10%10
baiwei=n//100
if 100<=n<1000:
    for i in range(100,n+1):
        if n==gewei**3+shiwei**3+baiwei**3:
            print(i)
elif n>=1000:
    for i in range(100,1000):
        if n==gewei**3+shiwei**3+baiwei**3:        
            print(i)
else:
    print("none")


