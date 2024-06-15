n=eval(input())
k=2
while k<=n-1:
    r=n%k
    if r==0:
        break
    else:
        k=k+1
if k==n:
    print(n)
else:
    print(n,"is not")
